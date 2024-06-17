# Handwriting visualizations
- stable version: 0.3.0

# Publishing to pypi
- Easiest way is to be on WSL2 or Linux distro
- Install **poetry**
- Rename file **_Makefile** to **Makefile**
- In the Makefile edit **YOUR_PYPI_TOKEN** with your generated pypi token
- In the same directory as this README file is run commands:

# FOR MAC
# Publishing to pypi
- Easiest way is to be on WSL2 or Linux distro
- Install **poetry**
- Rename file **_Makefile** to **Makefile**
- in make file keep only "
  publish:
	poetry publish --build
"
- nano ~/.zshrc
- export POETRY_PYPI_TOKEN_PYPI=YOUR_API_TOKEN
- source ~/.zshrc
- poetry config pypi-token.pypi YOUR_API_TOKEN
- make publish


```
make set_token
make publish
```

