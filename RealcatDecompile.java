import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

import generic.cache.CachingPool;
import generic.cache.CountingBasicFactory;
import generic.concurrent.QCallback;
import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.decompiler.DecompiledFunction;
import ghidra.app.decompiler.DecompileOptions.CommentStyleEnum;
import ghidra.app.decompiler.parallel.ChunkingParallelDecompiler;
import ghidra.app.decompiler.parallel.ParallelDecompiler;
import ghidra.app.script.GhidraScript;
import ghidra.app.util.DomainObjectService;
import ghidra.app.util.Option;
import ghidra.app.util.OptionException;
import ghidra.app.util.exporter.Exporter;
import ghidra.app.util.exporter.ExporterException;
import ghidra.framework.model.DomainObject;
import ghidra.framework.options.ToolOptions;
import ghidra.framework.plugintool.util.OptionsService;
import ghidra.program.model.address.Address;
import ghidra.program.model.address.AddressSetView;
import ghidra.program.model.data.DataOrganization;
import ghidra.program.model.data.DataTypeManager;
import ghidra.program.model.data.DataTypeWriter;
import ghidra.program.model.listing.CodeUnit;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.Listing;
import ghidra.program.model.listing.Program;
import ghidra.util.HelpLocation;
import ghidra.util.Msg;
import ghidra.util.exception.CancelledException;
import ghidra.util.task.CancelledListener;
import ghidra.util.task.TaskMonitor;
import ghidra.util.task.TaskMonitorAdapter;
import ghidra.util.xml.XmlAttributes;
import ghidra.util.xml.XmlWriter;

public class RealcatDecompile extends GhidraScript {
	public static class ReealCatCppExporter extends Exporter {

		public static final String SPLIT_FILE = "Split each function into individual file";
		public static final String CREATE_C_FILE = "Create C File (.c)";
		public static final String CREATE_HEADER_FILE = "Create Header File (.h)";
		public static final String USE_CPP_STYLE_COMMENTS = "Use C++ Style comments (//)";

		private static String EOL = System.getProperty("line.separator");

		private boolean isUseCppStyleComments = true;
		//private boolean isSplitFunctions   = false;
		private DecompileOptions options;
		private boolean userSuppliedOptions = false;

		public ReealCatCppExporter() {
			super("C/C++", "c", new HelpLocation("ExporterPlugin", "c_cpp"));
		}

		public ReealCatCppExporter(DecompileOptions options) {
			this();
			this.options = options;
			this.userSuppliedOptions = true;
		}

		@Override
		public boolean export(File file, DomainObject domainObj, AddressSetView addrSet,
				TaskMonitor monitor) throws IOException, ExporterException {
			if (!(domainObj instanceof Program)) {
				log.appendMsg("Unsupported type: " + domainObj.getClass().getName());
				return false;
			}

			Program program = (Program) domainObj;

			configureOptions(program);

			if (addrSet == null) {
				addrSet = program.getMemory();
			}
						
			XmlWriter w = new XmlWriter(file, null);
			w.startElement("ROOT");
			
			CachingPool<DecompInterface> decompilerPool =
				new CachingPool<>(new DecompilerFactory(program));
			ParallelDecompilerCallback callback = new ParallelDecompilerCallback(decompilerPool);
			ChunkingTaskMonitor chunkingMonitor = new ChunkingTaskMonitor(monitor);
			ChunkingParallelDecompiler<CPPResult> parallelDecompiler =
				ParallelDecompiler.createChunkingParallelDecopmiler(callback, chunkingMonitor);

			try {
				chunkingMonitor.checkCanceled();
				
				decompileAndExport(addrSet, program, w, parallelDecompiler,
					chunkingMonitor);
				
				return true;
			}
			catch (CancelledException e) {
				return false;
			}
			catch (Exception e) {
				Msg.error(this, "Error in parallel decompile task", e);
				return false;
			}
			finally {
				decompilerPool.dispose();
				parallelDecompiler.dispose();
			
				w.endElement("ROOT");
				w.close();
			}

		}

		private void decompileAndExport(AddressSetView addrSet, Program program,
				XmlWriter w,
				ChunkingParallelDecompiler<CPPResult> parallelDecompiler,
				ChunkingTaskMonitor chunkingMonitor)
				throws InterruptedException, Exception, CancelledException {

			int functionCount = program.getFunctionManager().getFunctionCount();
			chunkingMonitor.doInitialize(functionCount);

			Listing listing = program.getListing();
			FunctionIterator iterator = listing.getFunctions(addrSet, true);
			List<Function> functions = new ArrayList<>();
			for (int i = 0; iterator.hasNext(); i++) {
				//
				// Write results every so many items so that we don't blow out memory
				//
				if (i % 10000 == 0) {
					List<CPPResult> results = parallelDecompiler.decompileFunctions(functions);
					writeResults(results, w, chunkingMonitor);
					functions.clear();
				}

				functions.add(iterator.next());
			}

			// handle any remaining functions
			List<CPPResult> results = parallelDecompiler.decompileFunctions(functions);
			writeResults(results, w, chunkingMonitor);
		}

		private void writeResults(List<CPPResult> results, XmlWriter w, TaskMonitor monitor) throws CancelledException {
			monitor.checkCanceled();
						
			Collections.sort(results);

			StringBuilder headers = new StringBuilder();
			StringBuilder bodies = new StringBuilder();
			for (CPPResult entry : results) {
				monitor.checkCanceled();
				if (entry != null) {
					String headerCode = entry.getHeaderCode();
					if (headerCode != null) {
						headers.append(headerCode);
						headers.append(EOL);
					}
					
					String bodyCode = entry.getBodyCode();
					if (bodyCode != null) {
						XmlAttributes attr = new XmlAttributes();
						attr.addAttribute("address", entry.getAddress());
						w.writeElement("function", attr, bodyCode);
						bodies.append("[Function Address]" + entry.getAddress());//Ìí¼Óº¯ÊýµØÖ·
						bodies.append(bodyCode);
						bodies.append(EOL);
					}
				}
			}

			monitor.checkCanceled();
		}

		private void configureOptions(Program program) {
			if (!userSuppliedOptions) {
				options = new DecompileOptions();

				if (provider != null) {
					OptionsService service = provider.getService(OptionsService.class);
					if (service != null) {
						ToolOptions opt = service.getOptions("Decompiler");
						options.grabFromToolAndProgram(null, opt, program);
					}
				}

				if (isUseCppStyleComments) {
					options.setCommentStyle(CommentStyleEnum.CPPStyle);
				}
				else {
					options.setCommentStyle(CommentStyleEnum.CStyle);
				}
			}
		}

		@Override
		public List<Option> getOptions(DomainObjectService domainObjectService) {
			ArrayList<Option> list = new ArrayList<>();
			//list.add(new Option(SPLIT_FILE, new Boolean(isSplitFunctions)));
			list.add(new Option(USE_CPP_STYLE_COMMENTS, new Boolean(isUseCppStyleComments)));
			return list;
		}

		@Override
		public void setOptions(List<Option> options) throws OptionException {
			for (Option option : options) {
				String optName = option.getName();
				try {
					if (optName.equals(SPLIT_FILE)) {
						//isSplitFunctions = ((Boolean)option.getValue()).booleanValue();
					}
					else if (optName.equals(USE_CPP_STYLE_COMMENTS)) {
						isUseCppStyleComments = ((Boolean) option.getValue()).booleanValue();
					}
					else {
						throw new OptionException("Unknown option: " + optName);
					}
				}
				catch (ClassCastException e) {
					throw new OptionException(
						"Invalid type for option: " + optName + " - " + e.getMessage());
				}
			}
		}

	//==================================================================================================
	// Inner Classes
	//==================================================================================================

		private class CPPResult implements Comparable<CPPResult> {

			private Address address;
			private String bodyCode;
			private String headerCode;

			CPPResult(Address address, String headerCode, String bodyCode) {
				this.address = address;
				this.headerCode = headerCode;
				this.bodyCode = bodyCode;
			}

			String getHeaderCode() {
				return headerCode;
			}

			String getBodyCode() {
				return bodyCode;
			}
			
			String getAddress() {
				return address.toString();
			}

			@Override
			public int compareTo(CPPResult other) {
				return address.compareTo(other.address);
			}

		}

		private class DecompilerFactory extends CountingBasicFactory<DecompInterface> {

			private Program program;

			DecompilerFactory(Program program) {
				this.program = program;
			}

			@Override
			public DecompInterface doCreate(int itemNumber) throws IOException {
				DecompInterface decompiler = new DecompInterface();
				decompiler.setOptions(options);
				decompiler.openProgram(program);
				decompiler.toggleSyntaxTree(false);		// Don't need syntax tree
				return decompiler;
			}

			@Override
			public void doDispose(DecompInterface decompiler) {
				decompiler.dispose();
			}
		}

		private class ParallelDecompilerCallback implements QCallback<Function, CPPResult> {

			private CachingPool<DecompInterface> pool;

			ParallelDecompilerCallback(CachingPool<DecompInterface> decompilerPool) {
				this.pool = decompilerPool;
			}

			@Override
			public CPPResult process(Function function, TaskMonitor monitor) throws Exception {
				if (monitor.isCancelled()) {
					return null;
				}

				DecompInterface decompiler = pool.get();
				try {
					CPPResult result = doWork(function, decompiler, monitor);
					return result;
				}
				finally {
					pool.release(decompiler);
				}
			}

			private CPPResult doWork(Function function, DecompInterface decompiler,
					TaskMonitor monitor) {
				Address entryPoint = function.getEntryPoint();
				CodeUnit codeUnitAt = function.getProgram().getListing().getCodeUnitAt(entryPoint);
				if (codeUnitAt == null || !(codeUnitAt instanceof Instruction)) {
					return new CPPResult(entryPoint, function.getPrototypeString(false, false), null);
				}

				monitor.setMessage("Decompiling " + function.getName());

				DecompileResults dr =
					decompiler.decompileFunction(function, options.getDefaultTimeout(), monitor);
				String errorMessage = dr.getErrorMessage();
				if (!"".equals(errorMessage)) {
					Msg.warn(ReealCatCppExporter.this, "Error decompiling: " + errorMessage);
					if (options.isWARNCommentIncluded()) {
						monitor.incrementProgress(1);
						return new CPPResult(entryPoint, null,
							"/*" + EOL + "Unable to decompile '" + function.getName() + "'" + EOL +
								"Cause: " + errorMessage + EOL + "*/" + EOL);
					}
					return null;
				}

				DecompiledFunction decompiledFunction = dr.getDecompiledFunction();
				return new CPPResult(entryPoint, decompiledFunction.getSignature(),
					decompiledFunction.getC());
			}
		}

		/**
		 * A class that exists because we are doing something that the ConcurrentQ was not
		 * designed for--chunking.  We do not want out monitor being reset every time we start a new
		 * chunk. So, we wrap a real monitor, overriding the behavior such that initialize() has
		 * no effect when it is called by the queue.
		 */
		private class ChunkingTaskMonitor extends TaskMonitorAdapter {
			private TaskMonitor monitor;

			ChunkingTaskMonitor(TaskMonitor monitor) {
				this.monitor = monitor;
			}

			void doInitialize(long value) {
				// this lets us initialize when we want to
				monitor.initialize(value);
			}

			@Override
			public void setProgress(long value) {
				monitor.setProgress(value);
			}

			@Override
			public void checkCanceled() throws CancelledException {
				monitor.checkCanceled();
			}

			@Override
			public void setMessage(String message) {
				monitor.setMessage(message);
			}

			@Override
			public synchronized void addCancelledListener(CancelledListener listener) {
				monitor.addCancelledListener(listener);
			}

			@Override
			public synchronized void removeCancelledListener(CancelledListener listener) {
				monitor.removeCancelledListener(listener);
			}
		}
	}


	@Override
	protected void run() throws Exception {
		String[] args = this.getScriptArgs();		
		File outputFile = new File(args[0]);
		ReealCatCppExporter cppExporter = new ReealCatCppExporter();
		cppExporter.setExporterServiceProvider(state.getTool());
		cppExporter.export(outputFile, currentProgram, null, monitor);
		/*
		Scanner input = new Scanner(outputFile);
		while (input.hasNextLine())
	    {
			System.out.println(input.nextLine());
	    }*/ 
	}
}
