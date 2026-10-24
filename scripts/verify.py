"""Run the independent exact checks. Does not claim to rebuild Lean."""
from pathlib import Path
import argparse,os,shutil,subprocess,sys,tempfile

ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser()
ap.add_argument('--cc',help='C compiler path; defaults to cc, gcc or clang')
args=ap.parse_args()
logs=ROOT/'verification'/'current';logs.mkdir(parents=True,exist_ok=True)

def run(command,log):
    p=subprocess.run(list(map(str,command)),stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (logs/log).write_bytes(p.stdout)
    if p.returncode: raise SystemExit(p.stdout.decode(errors='replace'))
    return p.stdout.decode(errors='replace')

special=False
bundled=Path.home()/'.elan/toolchains/leanprover--lean4---v4.34.1/bin/clang.exe'
if os.name=='nt' and not args.cc and bundled.exists():
    cc=str(bundled);special=True
else:
    cc=args.cc or next((shutil.which(x) for x in ['cc','gcc','clang'] if shutil.which(x)),None)
if not cc: raise SystemExit('Install a C compiler or pass --cc PATH.')
if os.name=='nt' and '.elan' in Path(cc).resolve().parts:
    special=True
with tempfile.TemporaryDirectory(prefix='nilpotent-F3-',dir=logs) as tmp:
    assert Path(tmp).resolve().is_relative_to(logs.resolve())
    exe=Path(tmp)/('audit_tree.exe' if os.name=='nt' else 'audit_tree')
    source=ROOT/'verification/audit_tree.c'
    if special:
        lib=Path(cc).parents[1]/'lib'
        command=[cc,'--target=x86_64-w64-windows-gnu','-O3','-fno-stack-protector','-nostdlib',
                 '-Wl,--entry,mainCRTStartup',source,'-L'+str(lib),'-lmsvcrt','-lkernel32','-o',exe]
    else:
        command=[cc,'-O3','-std=c11','-DPORTABLE',source,'-o',exe]
    run(command,'c-build.txt')
    print(run([exe],'audit-tree.txt'))
print(run([sys.executable,ROOT/'verification/verify_examples.py'],'examples.json'))
print('Exact independent checks passed. For a full formal rebuild see README.md.')
