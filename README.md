# Using Python, Jupyter and Scripts


1. First clone repo: `git clone git@github.com:SamuelStori/tutorial.git`
2. `conda env create -f environment.yml`
3. Open shell
4. `jupyter notebook`
	- Maybe at first you want to check that you are running in the actual kernel that you want: `import sys; print(sys.executable)` or in the terminal: `jupyter kernelspec list`
5. Code
6. Share: `conda env export –-from-history > environment.yml`
	- We use the --from-history flag to make it work across platforms.

