# Fresh-clone verification — 2026-10-26

- Source commit: c46d4864e909e5d0834d0bfbd8a47575e4966128
- Clone directory: /private/tmp/gst-fresh-clone.tt1cDc
- Procedure: README commands, then documented site and Live smoke checks.

## 0. PyPI reachability
HTTP 200
exit: 0

## 1. Clone
Cloning into '/private/tmp/gst-fresh-clone.tt1cDc'...
exit: 0

## sh scripts/bootstrap.sh
Collecting annotated-types==0.8.0 (from -r requirements-lock.txt (line 1))
  Using cached annotated_types-0.8.0-py3-none-any.whl.metadata (15 kB)
Collecting anyio==4.15.1 (from -r requirements-lock.txt (line 2))
  Using cached anyio-4.15.1-py3-none-any.whl.metadata (4.7 kB)
Collecting attrs==26.1.0 (from -r requirements-lock.txt (line 3))
  Using cached attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting certifi==2026.10.18 (from -r requirements-lock.txt (line 4))
  Using cached certifi-2026.10.18-py3-none-any.whl.metadata (2.5 kB)
Collecting cffi==2.1.1 (from -r requirements-lock.txt (line 5))
  Downloading cffi-2.1.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (2.5 kB)
Collecting charset-normalizer==3.5.2 (from -r requirements-lock.txt (line 6))
  Downloading charset_normalizer-3.5.2-cp314-cp314-macosx_10_15_universal2.whl.metadata (46 kB)
Collecting click==8.5.0 (from -r requirements-lock.txt (line 7))
  Using cached click-8.5.0-py3-none-any.whl.metadata (2.6 kB)
Collecting contourpy==1.4.0 (from -r requirements-lock.txt (line 8))
  Downloading contourpy-1.4.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (3.8 kB)
Collecting cryptography==50.0.2 (from -r requirements-lock.txt (line 9))
  Using cached cryptography-50.0.2-cp311-abi3-macosx_11_0_arm64.whl.metadata (4.4 kB)
Collecting cycler==0.12.1 (from -r requirements-lock.txt (line 10))
  Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting distro==1.9.0 (from -r requirements-lock.txt (line 11))
  Using cached distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
Collecting fonttools==4.67.0 (from -r requirements-lock.txt (line 12))
  Downloading fonttools-4.67.0-cp314-cp314-macosx_10_15_universal2.whl.metadata (137 kB)
Collecting h11==0.16.0 (from -r requirements-lock.txt (line 13))
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting httpcore==1.0.9 (from -r requirements-lock.txt (line 14))
  Using cached httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting httpx==0.28.1 (from -r requirements-lock.txt (line 15))
  Using cached httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting idna==3.20 (from -r requirements-lock.txt (line 16))
  Using cached idna-3.20-py3-none-any.whl.metadata (7.2 kB)
Collecting itsdangerous==2.2.0 (from -r requirements-lock.txt (line 17))
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting Jinja2==3.1.6 (from -r requirements-lock.txt (line 18))
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting jiter==0.17.0 (from -r requirements-lock.txt (line 19))
  Downloading jiter-0.17.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (5.2 kB)
Collecting jsonschema==4.26.0 (from -r requirements-lock.txt (line 20))
  Using cached jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting jsonschema-specifications==2025.9.1 (from -r requirements-lock.txt (line 21))
  Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting kiwisolver==1.5.1 (from -r requirements-lock.txt (line 22))
  Downloading kiwisolver-1.5.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (5.2 kB)
Collecting MarkupSafe==3.0.4 (from -r requirements-lock.txt (line 23))
  Downloading markupsafe-3.0.4-cp314-cp314-macosx_11_0_arm64.whl.metadata (2.7 kB)
Collecting matplotlib==3.10.8 (from -r requirements-lock.txt (line 24))
  Downloading matplotlib-3.10.8-cp314-cp314-macosx_11_0_arm64.whl.metadata (52 kB)
Collecting numpy==2.5.4 (from -r requirements-lock.txt (line 25))
  Downloading numpy-2.5.4-cp314-cp314-macosx_14_0_arm64.whl.metadata (6.6 kB)
Collecting openai==2.54.0 (from -r requirements-lock.txt (line 26))
  Using cached openai-2.54.0-py3-none-any.whl.metadata (40 kB)
Collecting packaging==26.3 (from -r requirements-lock.txt (line 27))
  Using cached packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pandas==3.0.6 (from -r requirements-lock.txt (line 28))
  Downloading pandas-3.0.6-cp314-cp314-macosx_11_0_arm64.whl.metadata (79 kB)
Collecting pillow==12.3.0 (from -r requirements-lock.txt (line 29))
  Downloading pillow-12.3.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (9.1 kB)
Collecting pip-licenses==5.5.5 (from -r requirements-lock.txt (line 30))
  Using cached pip_licenses-5.5.5-py3-none-any.whl.metadata (35 kB)
Collecting prettytable==3.18.0 (from -r requirements-lock.txt (line 31))
  Using cached prettytable-3.18.0-py3-none-any.whl.metadata (37 kB)
Collecting protobuf==7.36.2 (from -r requirements-lock.txt (line 32))
  Using cached protobuf-7.36.2-cp310-abi3-macosx_10_9_universal2.whl.metadata (595 bytes)
Collecting pycparser==3.11 (from -r requirements-lock.txt (line 33))
  Using cached pycparser-3.11-py3-none-any.whl.metadata (8.2 kB)
Collecting pydantic==2.14.1 (from -r requirements-lock.txt (line 34))
  Using cached pydantic-2.14.1-py3-none-any.whl.metadata (133 kB)
Collecting pydantic_core==2.50.1 (from -r requirements-lock.txt (line 35))
  Downloading pydantic_core-2.50.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (6.5 kB)
Collecting pyexasol==2.4.1 (from -r requirements-lock.txt (line 36))
  Using cached pyexasol-2.4.1-py3-none-any.whl.metadata (4.7 kB)
Collecting pyparsing==3.3.3 (from -r requirements-lock.txt (line 37))
  Using cached pyparsing-3.3.3-py3-none-any.whl.metadata (5.9 kB)
Collecting python-dateutil==2.9.0.post0 (from -r requirements-lock.txt (line 38))
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting python-multipart==0.0.32 (from -r requirements-lock.txt (line 39))
  Using cached python_multipart-0.0.32-py3-none-any.whl.metadata (2.1 kB)
Collecting referencing==0.37.0 (from -r requirements-lock.txt (line 40))
  Using cached referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting requests==2.34.2 (from -r requirements-lock.txt (line 41))
  Using cached requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting rpds-py==2026.9.1 (from -r requirements-lock.txt (line 42))
  Downloading rpds_py-2026.9.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (4.1 kB)
Collecting six==1.17.0 (from -r requirements-lock.txt (line 43))
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting sniffio==1.3.1 (from -r requirements-lock.txt (line 44))
  Using cached sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting starlette==1.9.0 (from -r requirements-lock.txt (line 45))
  Using cached starlette-1.9.0-py3-none-any.whl.metadata (6.6 kB)
Collecting tqdm==4.70.1 (from -r requirements-lock.txt (line 46))
  Using cached tqdm-4.70.1-py3-none-any.whl.metadata (57 kB)
Collecting typing-inspection==0.4.4 (from -r requirements-lock.txt (line 47))
  Using cached typing_inspection-0.4.4-py3-none-any.whl.metadata (2.6 kB)
Collecting typing_extensions==4.16.0 (from -r requirements-lock.txt (line 48))
  Using cached typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Collecting urllib3==2.8.0 (from -r requirements-lock.txt (line 49))
  Using cached urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
Collecting uvicorn==0.54.0 (from -r requirements-lock.txt (line 50))
  Using cached uvicorn-0.54.0-py3-none-any.whl.metadata (6.6 kB)
Collecting wcwidth==0.9.3 (from -r requirements-lock.txt (line 51))
  Using cached wcwidth-0.9.3-cp310-abi3-macosx_11_0_arm64.whl.metadata (23 kB)
Collecting websocket-client==1.9.0 (from -r requirements-lock.txt (line 52))
  Using cached websocket_client-1.9.0-py3-none-any.whl.metadata (8.3 kB)
Collecting websockets==17.2 (from -r requirements-lock.txt (line 53))
  Downloading websockets-17.2-cp314-cp314-macosx_11_0_arm64.whl.metadata (6.3 kB)
Using cached annotated_types-0.8.0-py3-none-any.whl (13 kB)
Using cached anyio-4.15.1-py3-none-any.whl (132 kB)
Using cached attrs-26.1.0-py3-none-any.whl (67 kB)
Using cached certifi-2026.10.18-py3-none-any.whl (134 kB)
Downloading cffi-2.1.1-cp314-cp314-macosx_11_0_arm64.whl (184 kB)
Downloading charset_normalizer-3.5.2-cp314-cp314-macosx_10_15_universal2.whl (367 kB)
Using cached click-8.5.0-py3-none-any.whl (125 kB)
Downloading contourpy-1.4.0-cp314-cp314-macosx_11_0_arm64.whl (283 kB)
Using cached cryptography-50.0.2-cp311-abi3-macosx_11_0_arm64.whl (3.9 MB)
Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
Using cached distro-1.9.0-py3-none-any.whl (20 kB)
Downloading fonttools-4.67.0-cp314-cp314-macosx_10_15_universal2.whl (3.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 1.1 MB/s  0:00:02
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Using cached httpcore-1.0.9-py3-none-any.whl (78 kB)
Using cached httpx-0.28.1-py3-none-any.whl (73 kB)
Using cached idna-3.20-py3-none-any.whl (69 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading jiter-0.17.0-cp314-cp314-macosx_11_0_arm64.whl (321 kB)
Using cached jsonschema-4.26.0-py3-none-any.whl (90 kB)
Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Downloading kiwisolver-1.5.1-cp314-cp314-macosx_11_0_arm64.whl (64 kB)
Downloading markupsafe-3.0.4-cp314-cp314-macosx_11_0_arm64.whl (12 kB)
Downloading matplotlib-3.10.8-cp314-cp314-macosx_11_0_arm64.whl (8.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 MB 1.2 MB/s  0:00:06
Downloading numpy-2.5.4-cp314-cp314-macosx_14_0_arm64.whl (5.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 1.2 MB/s  0:00:04
Using cached openai-2.54.0-py3-none-any.whl (1.7 MB)
Using cached pydantic-2.14.1-py3-none-any.whl (488 kB)
Using cached typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Using cached packaging-26.3-py3-none-any.whl (129 kB)
Downloading pandas-3.0.6-cp314-cp314-macosx_11_0_arm64.whl (10.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.2/10.2 MB 1.1 MB/s  0:00:08
Downloading pillow-12.3.0-cp314-cp314-macosx_11_0_arm64.whl (4.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.8/4.8 MB 1.1 MB/s  0:00:04
Using cached pip_licenses-5.5.5-py3-none-any.whl (23 kB)
Using cached prettytable-3.18.0-py3-none-any.whl (37 kB)
Using cached protobuf-7.36.2-cp310-abi3-macosx_10_9_universal2.whl (456 kB)
Using cached pycparser-3.11-py3-none-any.whl (51 kB)
Downloading pydantic_core-2.50.1-cp314-cp314-macosx_11_0_arm64.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 1.2 MB/s  0:00:01
Using cached pyexasol-2.4.1-py3-none-any.whl (86 kB)
Using cached websocket_client-1.9.0-py3-none-any.whl (82 kB)
Using cached pyparsing-3.3.3-py3-none-any.whl (126 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached python_multipart-0.0.32-py3-none-any.whl (30 kB)
Using cached referencing-0.37.0-py3-none-any.whl (26 kB)
Using cached requests-2.34.2-py3-none-any.whl (73 kB)
Using cached urllib3-2.8.0-py3-none-any.whl (135 kB)
Downloading rpds_py-2026.9.1-cp314-cp314-macosx_11_0_arm64.whl (341 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
Using cached starlette-1.9.0-py3-none-any.whl (80 kB)
Using cached tqdm-4.70.1-py3-none-any.whl (80 kB)
Using cached typing_inspection-0.4.4-py3-none-any.whl (14 kB)
Using cached uvicorn-0.54.0-py3-none-any.whl (87 kB)
Using cached wcwidth-0.9.3-cp310-abi3-macosx_11_0_arm64.whl (610 kB)
Downloading websockets-17.2-cp314-cp314-macosx_11_0_arm64.whl (215 kB)
Installing collected packages: websockets, websocket-client, wcwidth, urllib3, typing_extensions, tqdm, sniffio, six, rpds-py, python-multipart, pyparsing, pycparser, protobuf, pillow, packaging, numpy, MarkupSafe, kiwisolver, jiter, itsdangerous, idna, h11, fonttools, distro, cycler, click, charset-normalizer, certifi, attrs, annotated-types, uvicorn, typing-inspection, requests, referencing, python-dateutil, pydantic_core, prettytable, Jinja2, httpcore, contourpy, cffi, anyio, starlette, pydantic, pip-licenses, pandas, matplotlib, jsonschema-specifications, httpx, cryptography, pyexasol, openai, jsonschema

Successfully installed Jinja2-3.1.6 MarkupSafe-3.0.4 annotated-types-0.8.0 anyio-4.15.1 attrs-26.1.0 certifi-2026.10.18 cffi-2.1.1 charset-normalizer-3.5.2 click-8.5.0 contourpy-1.4.0 cryptography-50.0.2 cycler-0.12.1 distro-1.9.0 fonttools-4.67.0 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 idna-3.20 itsdangerous-2.2.0 jiter-0.17.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 kiwisolver-1.5.1 matplotlib-3.10.8 numpy-2.5.4 openai-2.54.0 packaging-26.3 pandas-3.0.6 pillow-12.3.0 pip-licenses-5.5.5 prettytable-3.18.0 protobuf-7.36.2 pycparser-3.11 pydantic-2.14.1 pydantic_core-2.50.1 pyexasol-2.4.1 pyparsing-3.3.3 python-dateutil-2.9.0.post0 python-multipart-0.0.32 referencing-0.37.0 requests-2.34.2 rpds-py-2026.9.1 six-1.17.0 sniffio-1.3.1 starlette-1.9.0 tqdm-4.70.1 typing-inspection-0.4.4 typing_extensions-4.16.0 urllib3-2.8.0 uvicorn-0.54.0 wcwidth-0.9.3 websocket-client-1.9.0 websockets-17.2
exit: 0

## make provision-reader
sh scripts/bootstrap.sh
Requirement already satisfied: annotated-types==0.8.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 1)) (0.8.0)
Requirement already satisfied: anyio==4.15.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 2)) (4.15.1)
Requirement already satisfied: attrs==26.1.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 3)) (26.1.0)
Requirement already satisfied: certifi==2026.10.18 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 4)) (2026.10.18)
Requirement already satisfied: cffi==2.1.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 5)) (2.1.1)
Requirement already satisfied: charset-normalizer==3.5.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 6)) (3.5.2)
Requirement already satisfied: click==8.5.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 7)) (8.5.0)
Requirement already satisfied: contourpy==1.4.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 8)) (1.4.0)
Requirement already satisfied: cryptography==50.0.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 9)) (50.0.2)
Requirement already satisfied: cycler==0.12.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 10)) (0.12.1)
Requirement already satisfied: distro==1.9.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 11)) (1.9.0)
Requirement already satisfied: fonttools==4.67.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 12)) (4.67.0)
Requirement already satisfied: h11==0.16.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 13)) (0.16.0)
Requirement already satisfied: httpcore==1.0.9 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 14)) (1.0.9)
Requirement already satisfied: httpx==0.28.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 15)) (0.28.1)
Requirement already satisfied: idna==3.20 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 16)) (3.20)
Requirement already satisfied: itsdangerous==2.2.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 17)) (2.2.0)
Requirement already satisfied: Jinja2==3.1.6 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 18)) (3.1.6)
Requirement already satisfied: jiter==0.17.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 19)) (0.17.0)
Requirement already satisfied: jsonschema==4.26.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 20)) (4.26.0)
Requirement already satisfied: jsonschema-specifications==2025.9.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 21)) (2025.9.1)
Requirement already satisfied: kiwisolver==1.5.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 22)) (1.5.1)
Requirement already satisfied: MarkupSafe==3.0.4 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 23)) (3.0.4)
Requirement already satisfied: matplotlib==3.10.8 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 24)) (3.10.8)
Requirement already satisfied: numpy==2.5.4 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 25)) (2.5.4)
Requirement already satisfied: openai==2.54.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 26)) (2.54.0)
Requirement already satisfied: packaging==26.3 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 27)) (26.3)
Requirement already satisfied: pandas==3.0.6 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 28)) (3.0.6)
Requirement already satisfied: pillow==12.3.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 29)) (12.3.0)
Requirement already satisfied: pip-licenses==5.5.5 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 30)) (5.5.5)
Requirement already satisfied: prettytable==3.18.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 31)) (3.18.0)
Requirement already satisfied: protobuf==7.36.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 32)) (7.36.2)
Requirement already satisfied: pycparser==3.11 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 33)) (3.11)
Requirement already satisfied: pydantic==2.14.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 34)) (2.14.1)
Requirement already satisfied: pydantic_core==2.50.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 35)) (2.50.1)
Requirement already satisfied: pyexasol==2.4.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 36)) (2.4.1)
Requirement already satisfied: pyparsing==3.3.3 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 37)) (3.3.3)
Requirement already satisfied: python-dateutil==2.9.0.post0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 38)) (2.9.0.post0)
Requirement already satisfied: python-multipart==0.0.32 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 39)) (0.0.32)
Requirement already satisfied: referencing==0.37.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 40)) (0.37.0)
Requirement already satisfied: requests==2.34.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 41)) (2.34.2)
Requirement already satisfied: rpds-py==2026.9.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 42)) (2026.9.1)
Requirement already satisfied: six==1.17.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 43)) (1.17.0)
Requirement already satisfied: sniffio==1.3.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 44)) (1.3.1)
Requirement already satisfied: starlette==1.9.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 45)) (1.9.0)
Requirement already satisfied: tqdm==4.70.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 46)) (4.70.1)
Requirement already satisfied: typing-inspection==0.4.4 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 47)) (0.4.4)
Requirement already satisfied: typing_extensions==4.16.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 48)) (4.16.0)
Requirement already satisfied: urllib3==2.8.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 49)) (2.8.0)
Requirement already satisfied: uvicorn==0.54.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 50)) (0.54.0)
Requirement already satisfied: wcwidth==0.9.3 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 51)) (0.9.3)
Requirement already satisfied: websocket-client==1.9.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 52)) (1.9.0)
Requirement already satisfied: websockets==17.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 53)) (17.2)

[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: /private/tmp/gst-fresh-clone.tt1cDc/.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m src.provision_dashboard_reader
Traceback (most recent call last):
  File "<frozen runpy>", line 203, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/private/tmp/gst-fresh-clone.tt1cDc/src/provision_dashboard_reader.py", line 40, in <module>
    main()
    ~~~~^^
  File "/private/tmp/gst-fresh-clone.tt1cDc/src/provision_dashboard_reader.py", line 17, in main
    admin.execute(f'CREATE USER {USER} IDENTIFIED BY "{secret}"')
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/private/tmp/gst-fresh-clone.tt1cDc/.venv/lib/python3.14/site-packages/pyexasol/connection.py", line 342, in execute
    return self.cls_statement(self, query, query_params)
           ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/private/tmp/gst-fresh-clone.tt1cDc/.venv/lib/python3.14/site-packages/pyexasol/statement.py", line 110, in __init__
    self._execute()
    ~~~~~~~~~~~~~^^
  File "/private/tmp/gst-fresh-clone.tt1cDc/.venv/lib/python3.14/site-packages/pyexasol/statement.py", line 333, in _execute
    ret = self.connection.req(
        {
    ...<2 lines>...
        }
    )
  File "/private/tmp/gst-fresh-clone.tt1cDc/.venv/lib/python3.14/site-packages/pyexasol/connection.py", line 1424, in req
    raise cls_err(
    ...<4 lines>...
    )
pyexasol.exceptions.ExaQueryError:
(
    message     =>  user name DASHBOARD_READER conflicts with another user or role name (Session: 1880085351891927040)
    dsn         =>  localhost:8563
    user        =>  sys
    schema      =>
    session_id  =>  1880085351891927040
    code        =>  42500
    query       =>  CREATE USER DASHBOARD_READER IDENTIFIED BY "[REDACTED]"
)

make: *** [provision-reader] Error 1
exit: 2

## First attempt outcome

Failed during `make provision-reader`: an existing local `DASHBOARD_READER` account caused Exasol to report a conflicting username. The provisioning script recognised only a different error string and would have generated a new local secret. Fixed in the source checkout by accepting Exasol's conflict message, reusing the existing credential when present, and synchronising the account secret with `ALTER USER`. The first attempt did not proceed to data load, tests, site, or Live smoke; no tag was created.

# Fresh-clone retry — 2026-10-26

- Source commit: f76345bc4f1670a2e6c68db6418f9a9b800f02d6
- Clone directory: /private/tmp/gst-fresh-clone.2NekH0
- Procedure: README commands, then documented site and Live smoke checks.

## 0. PyPI reachability
HTTP/2 200
access-control-max-age: 86400
access-control-allow-origin: *
access-control-expose-headers: X-PyPI-Last-Serial
etag: "N0CYUXPHPOTnzbRcrEK8aQ"
referrer-policy: origin-when-cross-origin
content-security-policy: default-src 'none'; sandbox allow-top-navigation
x-pypi-last-serial: 42501245
server: gunicorn
cache-control: max-age=600, public
access-control-allow-methods: GET
access-control-allow-headers: Content-Type, If-Match, If-Modified-Since, If-None-Match, If-Unmodified-Since
accept-ranges: bytes
date: Mon, 26 Oct 2026 04:34:24 GMT
x-served-by: cache-iad-kiad7000171-IAD, cache-iad-kiad7000052-IAD, cache-del-vibw2260025-DEL
x-cache: MISS, HIT, HIT
x-cache-hits: 0, 201, 0
x-timer: S1792989264.497487,VS0,VE272
content-type: text/html
vary: Accept-Encoding, Accept
strict-transport-security: max-age=31536000; includeSubDomains; preload
x-frame-options: deny
x-xss-protection: 1; mode=block
x-content-type-options: nosniff
x-permitted-cross-domain-policies: none
permissions-policy: publickey-credentials-create=(self),publickey-credentials-get=(self),accelerometer=(),ambient-light-sensor=(),autoplay=(),battery=(),camera=(),display-capture=(),document-domain=(),encrypted-media=(),execution-while-not-rendered=(),execution-while-out-of-viewport=(),fullscreen=(),gamepad=(),geolocation=(),gyroscope=(),hid=(),identity-credentials-get=(),idle-detection=(),local-fonts=(),magnetometer=(),microphone=(),midi=(),otp-credentials=(),payment=(),picture-in-picture=(),screen-wake-lock=(),serial=(),speaker-selection=(),storage-access=(),usb=(),web-share=(),xr-spatial-tracking=()
content-length: 108381

exit: 0

## 1. Clone
Cloning into '/private/tmp/gst-fresh-clone.2NekH0'...
exit: 0

## sh scripts/bootstrap.sh
Collecting annotated-types==0.8.0 (from -r requirements-lock.txt (line 1))
  Using cached annotated_types-0.8.0-py3-none-any.whl.metadata (15 kB)
Collecting anyio==4.15.1 (from -r requirements-lock.txt (line 2))
  Using cached anyio-4.15.1-py3-none-any.whl.metadata (4.7 kB)
Collecting attrs==26.1.0 (from -r requirements-lock.txt (line 3))
  Using cached attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting certifi==2026.10.18 (from -r requirements-lock.txt (line 4))
  Using cached certifi-2026.10.18-py3-none-any.whl.metadata (2.5 kB)
Collecting cffi==2.1.1 (from -r requirements-lock.txt (line 5))
  Using cached cffi-2.1.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (2.5 kB)
Collecting charset-normalizer==3.5.2 (from -r requirements-lock.txt (line 6))
  Using cached charset_normalizer-3.5.2-cp314-cp314-macosx_10_15_universal2.whl.metadata (46 kB)
Collecting click==8.5.0 (from -r requirements-lock.txt (line 7))
  Using cached click-8.5.0-py3-none-any.whl.metadata (2.6 kB)
Collecting contourpy==1.4.0 (from -r requirements-lock.txt (line 8))
  Using cached contourpy-1.4.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (3.8 kB)
Collecting cryptography==50.0.2 (from -r requirements-lock.txt (line 9))
  Using cached cryptography-50.0.2-cp311-abi3-macosx_11_0_arm64.whl.metadata (4.4 kB)
Collecting cycler==0.12.1 (from -r requirements-lock.txt (line 10))
  Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting distro==1.9.0 (from -r requirements-lock.txt (line 11))
  Using cached distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
Collecting fonttools==4.67.0 (from -r requirements-lock.txt (line 12))
  Using cached fonttools-4.67.0-cp314-cp314-macosx_10_15_universal2.whl.metadata (137 kB)
Collecting h11==0.16.0 (from -r requirements-lock.txt (line 13))
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting httpcore==1.0.9 (from -r requirements-lock.txt (line 14))
  Using cached httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting httpx==0.28.1 (from -r requirements-lock.txt (line 15))
  Using cached httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting idna==3.20 (from -r requirements-lock.txt (line 16))
  Using cached idna-3.20-py3-none-any.whl.metadata (7.2 kB)
Collecting itsdangerous==2.2.0 (from -r requirements-lock.txt (line 17))
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting Jinja2==3.1.6 (from -r requirements-lock.txt (line 18))
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting jiter==0.17.0 (from -r requirements-lock.txt (line 19))
  Using cached jiter-0.17.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (5.2 kB)
Collecting jsonschema==4.26.0 (from -r requirements-lock.txt (line 20))
  Using cached jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting jsonschema-specifications==2025.9.1 (from -r requirements-lock.txt (line 21))
  Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting kiwisolver==1.5.1 (from -r requirements-lock.txt (line 22))
  Using cached kiwisolver-1.5.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (5.2 kB)
Collecting MarkupSafe==3.0.4 (from -r requirements-lock.txt (line 23))
  Using cached markupsafe-3.0.4-cp314-cp314-macosx_11_0_arm64.whl.metadata (2.7 kB)
Collecting matplotlib==3.10.8 (from -r requirements-lock.txt (line 24))
  Using cached matplotlib-3.10.8-cp314-cp314-macosx_11_0_arm64.whl.metadata (52 kB)
Collecting numpy==2.5.4 (from -r requirements-lock.txt (line 25))
  Using cached numpy-2.5.4-cp314-cp314-macosx_14_0_arm64.whl.metadata (6.6 kB)
Collecting openai==2.54.0 (from -r requirements-lock.txt (line 26))
  Using cached openai-2.54.0-py3-none-any.whl.metadata (40 kB)
Collecting packaging==26.3 (from -r requirements-lock.txt (line 27))
  Using cached packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pandas==3.0.6 (from -r requirements-lock.txt (line 28))
  Using cached pandas-3.0.6-cp314-cp314-macosx_11_0_arm64.whl.metadata (79 kB)
Collecting pillow==12.3.0 (from -r requirements-lock.txt (line 29))
  Using cached pillow-12.3.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (9.1 kB)
Collecting pip-licenses==5.5.5 (from -r requirements-lock.txt (line 30))
  Using cached pip_licenses-5.5.5-py3-none-any.whl.metadata (35 kB)
Collecting prettytable==3.18.0 (from -r requirements-lock.txt (line 31))
  Using cached prettytable-3.18.0-py3-none-any.whl.metadata (37 kB)
Collecting protobuf==7.36.2 (from -r requirements-lock.txt (line 32))
  Using cached protobuf-7.36.2-cp310-abi3-macosx_10_9_universal2.whl.metadata (595 bytes)
Collecting pycparser==3.11 (from -r requirements-lock.txt (line 33))
  Using cached pycparser-3.11-py3-none-any.whl.metadata (8.2 kB)
Collecting pydantic==2.14.1 (from -r requirements-lock.txt (line 34))
  Using cached pydantic-2.14.1-py3-none-any.whl.metadata (133 kB)
Collecting pydantic_core==2.50.1 (from -r requirements-lock.txt (line 35))
  Using cached pydantic_core-2.50.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (6.5 kB)
Collecting pyexasol==2.4.1 (from -r requirements-lock.txt (line 36))
  Using cached pyexasol-2.4.1-py3-none-any.whl.metadata (4.7 kB)
Collecting pyparsing==3.3.3 (from -r requirements-lock.txt (line 37))
  Using cached pyparsing-3.3.3-py3-none-any.whl.metadata (5.9 kB)
Collecting python-dateutil==2.9.0.post0 (from -r requirements-lock.txt (line 38))
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting python-multipart==0.0.32 (from -r requirements-lock.txt (line 39))
  Using cached python_multipart-0.0.32-py3-none-any.whl.metadata (2.1 kB)
Collecting referencing==0.37.0 (from -r requirements-lock.txt (line 40))
  Using cached referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting requests==2.34.2 (from -r requirements-lock.txt (line 41))
  Using cached requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting rpds-py==2026.9.1 (from -r requirements-lock.txt (line 42))
  Using cached rpds_py-2026.9.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (4.1 kB)
Collecting six==1.17.0 (from -r requirements-lock.txt (line 43))
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting sniffio==1.3.1 (from -r requirements-lock.txt (line 44))
  Using cached sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting starlette==1.9.0 (from -r requirements-lock.txt (line 45))
  Using cached starlette-1.9.0-py3-none-any.whl.metadata (6.6 kB)
Collecting tqdm==4.70.1 (from -r requirements-lock.txt (line 46))
  Using cached tqdm-4.70.1-py3-none-any.whl.metadata (57 kB)
Collecting typing-inspection==0.4.4 (from -r requirements-lock.txt (line 47))
  Using cached typing_inspection-0.4.4-py3-none-any.whl.metadata (2.6 kB)
Collecting typing_extensions==4.16.0 (from -r requirements-lock.txt (line 48))
  Using cached typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Collecting urllib3==2.8.0 (from -r requirements-lock.txt (line 49))
  Using cached urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
Collecting uvicorn==0.54.0 (from -r requirements-lock.txt (line 50))
  Using cached uvicorn-0.54.0-py3-none-any.whl.metadata (6.6 kB)
Collecting wcwidth==0.9.3 (from -r requirements-lock.txt (line 51))
  Using cached wcwidth-0.9.3-cp310-abi3-macosx_11_0_arm64.whl.metadata (23 kB)
Collecting websocket-client==1.9.0 (from -r requirements-lock.txt (line 52))
  Using cached websocket_client-1.9.0-py3-none-any.whl.metadata (8.3 kB)
Collecting websockets==17.2 (from -r requirements-lock.txt (line 53))
  Using cached websockets-17.2-cp314-cp314-macosx_11_0_arm64.whl.metadata (6.3 kB)
Using cached annotated_types-0.8.0-py3-none-any.whl (13 kB)
Using cached anyio-4.15.1-py3-none-any.whl (132 kB)
Using cached attrs-26.1.0-py3-none-any.whl (67 kB)
Using cached certifi-2026.10.18-py3-none-any.whl (134 kB)
Using cached cffi-2.1.1-cp314-cp314-macosx_11_0_arm64.whl (184 kB)
Using cached charset_normalizer-3.5.2-cp314-cp314-macosx_10_15_universal2.whl (367 kB)
Using cached click-8.5.0-py3-none-any.whl (125 kB)
Using cached contourpy-1.4.0-cp314-cp314-macosx_11_0_arm64.whl (283 kB)
Using cached cryptography-50.0.2-cp311-abi3-macosx_11_0_arm64.whl (3.9 MB)
Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
Using cached distro-1.9.0-py3-none-any.whl (20 kB)
Using cached fonttools-4.67.0-cp314-cp314-macosx_10_15_universal2.whl (3.1 MB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Using cached httpcore-1.0.9-py3-none-any.whl (78 kB)
Using cached httpx-0.28.1-py3-none-any.whl (73 kB)
Using cached idna-3.20-py3-none-any.whl (69 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached jiter-0.17.0-cp314-cp314-macosx_11_0_arm64.whl (321 kB)
Using cached jsonschema-4.26.0-py3-none-any.whl (90 kB)
Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Using cached kiwisolver-1.5.1-cp314-cp314-macosx_11_0_arm64.whl (64 kB)
Using cached markupsafe-3.0.4-cp314-cp314-macosx_11_0_arm64.whl (12 kB)
Using cached matplotlib-3.10.8-cp314-cp314-macosx_11_0_arm64.whl (8.2 MB)
Using cached numpy-2.5.4-cp314-cp314-macosx_14_0_arm64.whl (5.5 MB)
Using cached openai-2.54.0-py3-none-any.whl (1.7 MB)
Using cached pydantic-2.14.1-py3-none-any.whl (488 kB)
Using cached typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Using cached packaging-26.3-py3-none-any.whl (129 kB)
Using cached pandas-3.0.6-cp314-cp314-macosx_11_0_arm64.whl (10.2 MB)
Using cached pillow-12.3.0-cp314-cp314-macosx_11_0_arm64.whl (4.8 MB)
Using cached pip_licenses-5.5.5-py3-none-any.whl (23 kB)
Using cached prettytable-3.18.0-py3-none-any.whl (37 kB)
Using cached protobuf-7.36.2-cp310-abi3-macosx_10_9_universal2.whl (456 kB)
Using cached pycparser-3.11-py3-none-any.whl (51 kB)
Using cached pydantic_core-2.50.1-cp314-cp314-macosx_11_0_arm64.whl (2.0 MB)
Using cached pyexasol-2.4.1-py3-none-any.whl (86 kB)
Using cached websocket_client-1.9.0-py3-none-any.whl (82 kB)
Using cached pyparsing-3.3.3-py3-none-any.whl (126 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached python_multipart-0.0.32-py3-none-any.whl (30 kB)
Using cached referencing-0.37.0-py3-none-any.whl (26 kB)
Using cached requests-2.34.2-py3-none-any.whl (73 kB)
Using cached urllib3-2.8.0-py3-none-any.whl (135 kB)
Using cached rpds_py-2026.9.1-cp314-cp314-macosx_11_0_arm64.whl (341 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
Using cached starlette-1.9.0-py3-none-any.whl (80 kB)
Using cached tqdm-4.70.1-py3-none-any.whl (80 kB)
Using cached typing_inspection-0.4.4-py3-none-any.whl (14 kB)
Using cached uvicorn-0.54.0-py3-none-any.whl (87 kB)
Using cached wcwidth-0.9.3-cp310-abi3-macosx_11_0_arm64.whl (610 kB)
Using cached websockets-17.2-cp314-cp314-macosx_11_0_arm64.whl (215 kB)
Installing collected packages: websockets, websocket-client, wcwidth, urllib3, typing_extensions, tqdm, sniffio, six, rpds-py, python-multipart, pyparsing, pycparser, protobuf, pillow, packaging, numpy, MarkupSafe, kiwisolver, jiter, itsdangerous, idna, h11, fonttools, distro, cycler, click, charset-normalizer, certifi, attrs, annotated-types, uvicorn, typing-inspection, requests, referencing, python-dateutil, pydantic_core, prettytable, Jinja2, httpcore, contourpy, cffi, anyio, starlette, pydantic, pip-licenses, pandas, matplotlib, jsonschema-specifications, httpx, cryptography, pyexasol, openai, jsonschema

Successfully installed Jinja2-3.1.6 MarkupSafe-3.0.4 annotated-types-0.8.0 anyio-4.15.1 attrs-26.1.0 certifi-2026.10.18 cffi-2.1.1 charset-normalizer-3.5.2 click-8.5.0 contourpy-1.4.0 cryptography-50.0.2 cycler-0.12.1 distro-1.9.0 fonttools-4.67.0 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 idna-3.20 itsdangerous-2.2.0 jiter-0.17.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 kiwisolver-1.5.1 matplotlib-3.10.8 numpy-2.5.4 openai-2.54.0 packaging-26.3 pandas-3.0.6 pillow-12.3.0 pip-licenses-5.5.5 prettytable-3.18.0 protobuf-7.36.2 pycparser-3.11 pydantic-2.14.1 pydantic_core-2.50.1 pyexasol-2.4.1 pyparsing-3.3.3 python-dateutil-2.9.0.post0 python-multipart-0.0.32 referencing-0.37.0 requests-2.34.2 rpds-py-2026.9.1 six-1.17.0 sniffio-1.3.1 starlette-1.9.0 tqdm-4.70.1 typing-inspection-0.4.4 typing_extensions-4.16.0 urllib3-2.8.0 uvicorn-0.54.0 wcwidth-0.9.3 websocket-client-1.9.0 websockets-17.2

[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: /private/tmp/gst-fresh-clone.2NekH0/.venv/bin/python -m pip install --upgrade pip
zsh:18: read-only variable: status

## Retry harness outcome

The retry installed the locked dependencies in a new virtual environment, then stopped before provisioning because the verification harness used zsh's read-only `status` parameter. This was a harness error, not a project command failure. The next retry uses a different variable name. No tag was created.

# Fresh-clone final retry — 2026-10-26

- Source commit: f76345bc4f1670a2e6c68db6418f9a9b800f02d6
- Clone directory: /private/tmp/gst-fresh-clone.ENfI58
- Procedure: README commands, then documented site and Live smoke checks.

## 0. PyPI reachability
HTTP/2 200
access-control-max-age: 86400
access-control-allow-origin: *
access-control-expose-headers: X-PyPI-Last-Serial
etag: "N0CYUXPHPOTnzbRcrEK8aQ"
referrer-policy: origin-when-cross-origin
content-security-policy: default-src 'none'; sandbox allow-top-navigation
x-pypi-last-serial: 42501245
server: gunicorn
cache-control: max-age=600, public
access-control-allow-methods: GET
access-control-allow-headers: Content-Type, If-Match, If-Modified-Since, If-None-Match, If-Unmodified-Since
accept-ranges: bytes
date: Mon, 26 Oct 2026 04:34:58 GMT
x-served-by: cache-iad-kiad7000171-IAD, cache-iad-kiad7000052-IAD, cache-del-vibw2260039-DEL
x-cache: MISS, HIT, HIT
x-cache-hits: 0, 201, 1
x-timer: S1792989299.972855,VS0,VE1
content-type: text/html
vary: Accept-Encoding, Accept
strict-transport-security: max-age=31536000; includeSubDomains; preload
x-frame-options: deny
x-xss-protection: 1; mode=block
x-content-type-options: nosniff
x-permitted-cross-domain-policies: none
permissions-policy: publickey-credentials-create=(self),publickey-credentials-get=(self),accelerometer=(),ambient-light-sensor=(),autoplay=(),battery=(),camera=(),display-capture=(),document-domain=(),encrypted-media=(),execution-while-not-rendered=(),execution-while-out-of-viewport=(),fullscreen=(),gamepad=(),geolocation=(),gyroscope=(),hid=(),identity-credentials-get=(),idle-detection=(),local-fonts=(),magnetometer=(),microphone=(),midi=(),otp-credentials=(),payment=(),picture-in-picture=(),screen-wake-lock=(),serial=(),speaker-selection=(),storage-access=(),usb=(),web-share=(),xr-spatial-tracking=()
content-length: 108381

exit: 0

## 1. Clone
Cloning into '/private/tmp/gst-fresh-clone.ENfI58'...
exit: 0

## sh scripts/bootstrap.sh
Collecting annotated-types==0.8.0 (from -r requirements-lock.txt (line 1))
  Using cached annotated_types-0.8.0-py3-none-any.whl.metadata (15 kB)
Collecting anyio==4.15.1 (from -r requirements-lock.txt (line 2))
  Using cached anyio-4.15.1-py3-none-any.whl.metadata (4.7 kB)
Collecting attrs==26.1.0 (from -r requirements-lock.txt (line 3))
  Using cached attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting certifi==2026.10.18 (from -r requirements-lock.txt (line 4))
  Using cached certifi-2026.10.18-py3-none-any.whl.metadata (2.5 kB)
Collecting cffi==2.1.1 (from -r requirements-lock.txt (line 5))
  Using cached cffi-2.1.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (2.5 kB)
Collecting charset-normalizer==3.5.2 (from -r requirements-lock.txt (line 6))
  Using cached charset_normalizer-3.5.2-cp314-cp314-macosx_10_15_universal2.whl.metadata (46 kB)
Collecting click==8.5.0 (from -r requirements-lock.txt (line 7))
  Using cached click-8.5.0-py3-none-any.whl.metadata (2.6 kB)
Collecting contourpy==1.4.0 (from -r requirements-lock.txt (line 8))
  Using cached contourpy-1.4.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (3.8 kB)
Collecting cryptography==50.0.2 (from -r requirements-lock.txt (line 9))
  Using cached cryptography-50.0.2-cp311-abi3-macosx_11_0_arm64.whl.metadata (4.4 kB)
Collecting cycler==0.12.1 (from -r requirements-lock.txt (line 10))
  Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting distro==1.9.0 (from -r requirements-lock.txt (line 11))
  Using cached distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
Collecting fonttools==4.67.0 (from -r requirements-lock.txt (line 12))
  Using cached fonttools-4.67.0-cp314-cp314-macosx_10_15_universal2.whl.metadata (137 kB)
Collecting h11==0.16.0 (from -r requirements-lock.txt (line 13))
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting httpcore==1.0.9 (from -r requirements-lock.txt (line 14))
  Using cached httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting httpx==0.28.1 (from -r requirements-lock.txt (line 15))
  Using cached httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting idna==3.20 (from -r requirements-lock.txt (line 16))
  Using cached idna-3.20-py3-none-any.whl.metadata (7.2 kB)
Collecting itsdangerous==2.2.0 (from -r requirements-lock.txt (line 17))
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting Jinja2==3.1.6 (from -r requirements-lock.txt (line 18))
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting jiter==0.17.0 (from -r requirements-lock.txt (line 19))
  Using cached jiter-0.17.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (5.2 kB)
Collecting jsonschema==4.26.0 (from -r requirements-lock.txt (line 20))
  Using cached jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting jsonschema-specifications==2025.9.1 (from -r requirements-lock.txt (line 21))
  Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting kiwisolver==1.5.1 (from -r requirements-lock.txt (line 22))
  Using cached kiwisolver-1.5.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (5.2 kB)
Collecting MarkupSafe==3.0.4 (from -r requirements-lock.txt (line 23))
  Using cached markupsafe-3.0.4-cp314-cp314-macosx_11_0_arm64.whl.metadata (2.7 kB)
Collecting matplotlib==3.10.8 (from -r requirements-lock.txt (line 24))
  Using cached matplotlib-3.10.8-cp314-cp314-macosx_11_0_arm64.whl.metadata (52 kB)
Collecting numpy==2.5.4 (from -r requirements-lock.txt (line 25))
  Using cached numpy-2.5.4-cp314-cp314-macosx_14_0_arm64.whl.metadata (6.6 kB)
Collecting openai==2.54.0 (from -r requirements-lock.txt (line 26))
  Using cached openai-2.54.0-py3-none-any.whl.metadata (40 kB)
Collecting packaging==26.3 (from -r requirements-lock.txt (line 27))
  Using cached packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pandas==3.0.6 (from -r requirements-lock.txt (line 28))
  Using cached pandas-3.0.6-cp314-cp314-macosx_11_0_arm64.whl.metadata (79 kB)
Collecting pillow==12.3.0 (from -r requirements-lock.txt (line 29))
  Using cached pillow-12.3.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (9.1 kB)
Collecting pip-licenses==5.5.5 (from -r requirements-lock.txt (line 30))
  Using cached pip_licenses-5.5.5-py3-none-any.whl.metadata (35 kB)
Collecting prettytable==3.18.0 (from -r requirements-lock.txt (line 31))
  Using cached prettytable-3.18.0-py3-none-any.whl.metadata (37 kB)
Collecting protobuf==7.36.2 (from -r requirements-lock.txt (line 32))
  Using cached protobuf-7.36.2-cp310-abi3-macosx_10_9_universal2.whl.metadata (595 bytes)
Collecting pycparser==3.11 (from -r requirements-lock.txt (line 33))
  Using cached pycparser-3.11-py3-none-any.whl.metadata (8.2 kB)
Collecting pydantic==2.14.1 (from -r requirements-lock.txt (line 34))
  Using cached pydantic-2.14.1-py3-none-any.whl.metadata (133 kB)
Collecting pydantic_core==2.50.1 (from -r requirements-lock.txt (line 35))
  Using cached pydantic_core-2.50.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (6.5 kB)
Collecting pyexasol==2.4.1 (from -r requirements-lock.txt (line 36))
  Using cached pyexasol-2.4.1-py3-none-any.whl.metadata (4.7 kB)
Collecting pyparsing==3.3.3 (from -r requirements-lock.txt (line 37))
  Using cached pyparsing-3.3.3-py3-none-any.whl.metadata (5.9 kB)
Collecting python-dateutil==2.9.0.post0 (from -r requirements-lock.txt (line 38))
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting python-multipart==0.0.32 (from -r requirements-lock.txt (line 39))
  Using cached python_multipart-0.0.32-py3-none-any.whl.metadata (2.1 kB)
Collecting referencing==0.37.0 (from -r requirements-lock.txt (line 40))
  Using cached referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting requests==2.34.2 (from -r requirements-lock.txt (line 41))
  Using cached requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting rpds-py==2026.9.1 (from -r requirements-lock.txt (line 42))
  Using cached rpds_py-2026.9.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (4.1 kB)
Collecting six==1.17.0 (from -r requirements-lock.txt (line 43))
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting sniffio==1.3.1 (from -r requirements-lock.txt (line 44))
  Using cached sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting starlette==1.9.0 (from -r requirements-lock.txt (line 45))
  Using cached starlette-1.9.0-py3-none-any.whl.metadata (6.6 kB)
Collecting tqdm==4.70.1 (from -r requirements-lock.txt (line 46))
  Using cached tqdm-4.70.1-py3-none-any.whl.metadata (57 kB)
Collecting typing-inspection==0.4.4 (from -r requirements-lock.txt (line 47))
  Using cached typing_inspection-0.4.4-py3-none-any.whl.metadata (2.6 kB)
Collecting typing_extensions==4.16.0 (from -r requirements-lock.txt (line 48))
  Using cached typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Collecting urllib3==2.8.0 (from -r requirements-lock.txt (line 49))
  Using cached urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
Collecting uvicorn==0.54.0 (from -r requirements-lock.txt (line 50))
  Using cached uvicorn-0.54.0-py3-none-any.whl.metadata (6.6 kB)
Collecting wcwidth==0.9.3 (from -r requirements-lock.txt (line 51))
  Using cached wcwidth-0.9.3-cp310-abi3-macosx_11_0_arm64.whl.metadata (23 kB)
Collecting websocket-client==1.9.0 (from -r requirements-lock.txt (line 52))
  Using cached websocket_client-1.9.0-py3-none-any.whl.metadata (8.3 kB)
Collecting websockets==17.2 (from -r requirements-lock.txt (line 53))
  Using cached websockets-17.2-cp314-cp314-macosx_11_0_arm64.whl.metadata (6.3 kB)
Using cached annotated_types-0.8.0-py3-none-any.whl (13 kB)
Using cached anyio-4.15.1-py3-none-any.whl (132 kB)
Using cached attrs-26.1.0-py3-none-any.whl (67 kB)
Using cached certifi-2026.10.18-py3-none-any.whl (134 kB)
Using cached cffi-2.1.1-cp314-cp314-macosx_11_0_arm64.whl (184 kB)
Using cached charset_normalizer-3.5.2-cp314-cp314-macosx_10_15_universal2.whl (367 kB)
Using cached click-8.5.0-py3-none-any.whl (125 kB)
Using cached contourpy-1.4.0-cp314-cp314-macosx_11_0_arm64.whl (283 kB)
Using cached cryptography-50.0.2-cp311-abi3-macosx_11_0_arm64.whl (3.9 MB)
Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
Using cached distro-1.9.0-py3-none-any.whl (20 kB)
Using cached fonttools-4.67.0-cp314-cp314-macosx_10_15_universal2.whl (3.1 MB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Using cached httpcore-1.0.9-py3-none-any.whl (78 kB)
Using cached httpx-0.28.1-py3-none-any.whl (73 kB)
Using cached idna-3.20-py3-none-any.whl (69 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached jiter-0.17.0-cp314-cp314-macosx_11_0_arm64.whl (321 kB)
Using cached jsonschema-4.26.0-py3-none-any.whl (90 kB)
Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Using cached kiwisolver-1.5.1-cp314-cp314-macosx_11_0_arm64.whl (64 kB)
Using cached markupsafe-3.0.4-cp314-cp314-macosx_11_0_arm64.whl (12 kB)
Using cached matplotlib-3.10.8-cp314-cp314-macosx_11_0_arm64.whl (8.2 MB)
Using cached numpy-2.5.4-cp314-cp314-macosx_14_0_arm64.whl (5.5 MB)
Using cached openai-2.54.0-py3-none-any.whl (1.7 MB)
Using cached pydantic-2.14.1-py3-none-any.whl (488 kB)
Using cached typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Using cached packaging-26.3-py3-none-any.whl (129 kB)
Using cached pandas-3.0.6-cp314-cp314-macosx_11_0_arm64.whl (10.2 MB)
Using cached pillow-12.3.0-cp314-cp314-macosx_11_0_arm64.whl (4.8 MB)
Using cached pip_licenses-5.5.5-py3-none-any.whl (23 kB)
Using cached prettytable-3.18.0-py3-none-any.whl (37 kB)
Using cached protobuf-7.36.2-cp310-abi3-macosx_10_9_universal2.whl (456 kB)
Using cached pycparser-3.11-py3-none-any.whl (51 kB)
Using cached pydantic_core-2.50.1-cp314-cp314-macosx_11_0_arm64.whl (2.0 MB)
Using cached pyexasol-2.4.1-py3-none-any.whl (86 kB)
Using cached websocket_client-1.9.0-py3-none-any.whl (82 kB)
Using cached pyparsing-3.3.3-py3-none-any.whl (126 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached python_multipart-0.0.32-py3-none-any.whl (30 kB)
Using cached referencing-0.37.0-py3-none-any.whl (26 kB)
Using cached requests-2.34.2-py3-none-any.whl (73 kB)
Using cached urllib3-2.8.0-py3-none-any.whl (135 kB)
Using cached rpds_py-2026.9.1-cp314-cp314-macosx_11_0_arm64.whl (341 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
Using cached starlette-1.9.0-py3-none-any.whl (80 kB)
Using cached tqdm-4.70.1-py3-none-any.whl (80 kB)
Using cached typing_inspection-0.4.4-py3-none-any.whl (14 kB)
Using cached uvicorn-0.54.0-py3-none-any.whl (87 kB)
Using cached wcwidth-0.9.3-cp310-abi3-macosx_11_0_arm64.whl (610 kB)
Using cached websockets-17.2-cp314-cp314-macosx_11_0_arm64.whl (215 kB)
Installing collected packages: websockets, websocket-client, wcwidth, urllib3, typing_extensions, tqdm, sniffio, six, rpds-py, python-multipart, pyparsing, pycparser, protobuf, pillow, packaging, numpy, MarkupSafe, kiwisolver, jiter, itsdangerous, idna, h11, fonttools, distro, cycler, click, charset-normalizer, certifi, attrs, annotated-types, uvicorn, typing-inspection, requests, referencing, python-dateutil, pydantic_core, prettytable, Jinja2, httpcore, contourpy, cffi, anyio, starlette, pydantic, pip-licenses, pandas, matplotlib, jsonschema-specifications, httpx, cryptography, pyexasol, openai, jsonschema

Successfully installed Jinja2-3.1.6 MarkupSafe-3.0.4 annotated-types-0.8.0 anyio-4.15.1 attrs-26.1.0 certifi-2026.10.18 cffi-2.1.1 charset-normalizer-3.5.2 click-8.5.0 contourpy-1.4.0 cryptography-50.0.2 cycler-0.12.1 distro-1.9.0 fonttools-4.67.0 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 idna-3.20 itsdangerous-2.2.0 jiter-0.17.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 kiwisolver-1.5.1 matplotlib-3.10.8 numpy-2.5.4 openai-2.54.0 packaging-26.3 pandas-3.0.6 pillow-12.3.0 pip-licenses-5.5.5 prettytable-3.18.0 protobuf-7.36.2 pycparser-3.11 pydantic-2.14.1 pydantic_core-2.50.1 pyexasol-2.4.1 pyparsing-3.3.3 python-dateutil-2.9.0.post0 python-multipart-0.0.32 referencing-0.37.0 requests-2.34.2 rpds-py-2026.9.1 six-1.17.0 sniffio-1.3.1 starlette-1.9.0 tqdm-4.70.1 typing-inspection-0.4.4 typing_extensions-4.16.0 urllib3-2.8.0 uvicorn-0.54.0 wcwidth-0.9.3 websocket-client-1.9.0 websockets-17.2

[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: /private/tmp/gst-fresh-clone.ENfI58/.venv/bin/python -m pip install --upgrade pip
exit: 0

## make provision-reader
sh scripts/bootstrap.sh
Requirement already satisfied: annotated-types==0.8.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 1)) (0.8.0)
Requirement already satisfied: anyio==4.15.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 2)) (4.15.1)
Requirement already satisfied: attrs==26.1.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 3)) (26.1.0)
Requirement already satisfied: certifi==2026.10.18 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 4)) (2026.10.18)
Requirement already satisfied: cffi==2.1.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 5)) (2.1.1)
Requirement already satisfied: charset-normalizer==3.5.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 6)) (3.5.2)
Requirement already satisfied: click==8.5.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 7)) (8.5.0)
Requirement already satisfied: contourpy==1.4.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 8)) (1.4.0)
Requirement already satisfied: cryptography==50.0.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 9)) (50.0.2)
Requirement already satisfied: cycler==0.12.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 10)) (0.12.1)
Requirement already satisfied: distro==1.9.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 11)) (1.9.0)
Requirement already satisfied: fonttools==4.67.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 12)) (4.67.0)
Requirement already satisfied: h11==0.16.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 13)) (0.16.0)
Requirement already satisfied: httpcore==1.0.9 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 14)) (1.0.9)
Requirement already satisfied: httpx==0.28.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 15)) (0.28.1)
Requirement already satisfied: idna==3.20 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 16)) (3.20)
Requirement already satisfied: itsdangerous==2.2.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 17)) (2.2.0)
Requirement already satisfied: Jinja2==3.1.6 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 18)) (3.1.6)
Requirement already satisfied: jiter==0.17.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 19)) (0.17.0)
Requirement already satisfied: jsonschema==4.26.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 20)) (4.26.0)
Requirement already satisfied: jsonschema-specifications==2025.9.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 21)) (2025.9.1)
Requirement already satisfied: kiwisolver==1.5.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 22)) (1.5.1)
Requirement already satisfied: MarkupSafe==3.0.4 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 23)) (3.0.4)
Requirement already satisfied: matplotlib==3.10.8 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 24)) (3.10.8)
Requirement already satisfied: numpy==2.5.4 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 25)) (2.5.4)
Requirement already satisfied: openai==2.54.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 26)) (2.54.0)
Requirement already satisfied: packaging==26.3 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 27)) (26.3)
Requirement already satisfied: pandas==3.0.6 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 28)) (3.0.6)
Requirement already satisfied: pillow==12.3.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 29)) (12.3.0)
Requirement already satisfied: pip-licenses==5.5.5 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 30)) (5.5.5)
Requirement already satisfied: prettytable==3.18.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 31)) (3.18.0)
Requirement already satisfied: protobuf==7.36.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 32)) (7.36.2)
Requirement already satisfied: pycparser==3.11 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 33)) (3.11)
Requirement already satisfied: pydantic==2.14.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 34)) (2.14.1)
Requirement already satisfied: pydantic_core==2.50.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 35)) (2.50.1)
Requirement already satisfied: pyexasol==2.4.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 36)) (2.4.1)
Requirement already satisfied: pyparsing==3.3.3 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 37)) (3.3.3)
Requirement already satisfied: python-dateutil==2.9.0.post0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 38)) (2.9.0.post0)
Requirement already satisfied: python-multipart==0.0.32 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 39)) (0.0.32)
Requirement already satisfied: referencing==0.37.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 40)) (0.37.0)
Requirement already satisfied: requests==2.34.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 41)) (2.34.2)
Requirement already satisfied: rpds-py==2026.9.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 42)) (2026.9.1)
Requirement already satisfied: six==1.17.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 43)) (1.17.0)
Requirement already satisfied: sniffio==1.3.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 44)) (1.3.1)
Requirement already satisfied: starlette==1.9.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 45)) (1.9.0)
Requirement already satisfied: tqdm==4.70.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 46)) (4.70.1)
Requirement already satisfied: typing-inspection==0.4.4 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 47)) (0.4.4)
Requirement already satisfied: typing_extensions==4.16.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 48)) (4.16.0)
Requirement already satisfied: urllib3==2.8.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 49)) (2.8.0)
Requirement already satisfied: uvicorn==0.54.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 50)) (0.54.0)
Requirement already satisfied: wcwidth==0.9.3 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 51)) (0.9.3)
Requirement already satisfied: websocket-client==1.9.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 52)) (1.9.0)
Requirement already satisfied: websockets==17.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 53)) (17.2)

[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: /private/tmp/gst-fresh-clone.ENfI58/.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m src.provision_dashboard_reader
DASHBOARD_READER configured; label-free view grants are applied after reconciliation views exist. Secret was not printed.
exit: 0

## make test
sh scripts/bootstrap.sh
Requirement already satisfied: annotated-types==0.8.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 1)) (0.8.0)
Requirement already satisfied: anyio==4.15.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 2)) (4.15.1)
Requirement already satisfied: attrs==26.1.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 3)) (26.1.0)
Requirement already satisfied: certifi==2026.10.18 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 4)) (2026.10.18)
Requirement already satisfied: cffi==2.1.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 5)) (2.1.1)
Requirement already satisfied: charset-normalizer==3.5.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 6)) (3.5.2)
Requirement already satisfied: click==8.5.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 7)) (8.5.0)
Requirement already satisfied: contourpy==1.4.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 8)) (1.4.0)
Requirement already satisfied: cryptography==50.0.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 9)) (50.0.2)
Requirement already satisfied: cycler==0.12.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 10)) (0.12.1)
Requirement already satisfied: distro==1.9.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 11)) (1.9.0)
Requirement already satisfied: fonttools==4.67.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 12)) (4.67.0)
Requirement already satisfied: h11==0.16.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 13)) (0.16.0)
Requirement already satisfied: httpcore==1.0.9 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 14)) (1.0.9)
Requirement already satisfied: httpx==0.28.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 15)) (0.28.1)
Requirement already satisfied: idna==3.20 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 16)) (3.20)
Requirement already satisfied: itsdangerous==2.2.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 17)) (2.2.0)
Requirement already satisfied: Jinja2==3.1.6 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 18)) (3.1.6)
Requirement already satisfied: jiter==0.17.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 19)) (0.17.0)
Requirement already satisfied: jsonschema==4.26.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 20)) (4.26.0)
Requirement already satisfied: jsonschema-specifications==2025.9.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 21)) (2025.9.1)
Requirement already satisfied: kiwisolver==1.5.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 22)) (1.5.1)
Requirement already satisfied: MarkupSafe==3.0.4 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 23)) (3.0.4)
Requirement already satisfied: matplotlib==3.10.8 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 24)) (3.10.8)
Requirement already satisfied: numpy==2.5.4 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 25)) (2.5.4)
Requirement already satisfied: openai==2.54.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 26)) (2.54.0)
Requirement already satisfied: packaging==26.3 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 27)) (26.3)
Requirement already satisfied: pandas==3.0.6 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 28)) (3.0.6)
Requirement already satisfied: pillow==12.3.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 29)) (12.3.0)
Requirement already satisfied: pip-licenses==5.5.5 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 30)) (5.5.5)
Requirement already satisfied: prettytable==3.18.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 31)) (3.18.0)
Requirement already satisfied: protobuf==7.36.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 32)) (7.36.2)
Requirement already satisfied: pycparser==3.11 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 33)) (3.11)
Requirement already satisfied: pydantic==2.14.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 34)) (2.14.1)
Requirement already satisfied: pydantic_core==2.50.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 35)) (2.50.1)
Requirement already satisfied: pyexasol==2.4.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 36)) (2.4.1)
Requirement already satisfied: pyparsing==3.3.3 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 37)) (3.3.3)
Requirement already satisfied: python-dateutil==2.9.0.post0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 38)) (2.9.0.post0)
Requirement already satisfied: python-multipart==0.0.32 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 39)) (0.0.32)
Requirement already satisfied: referencing==0.37.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 40)) (0.37.0)
Requirement already satisfied: requests==2.34.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 41)) (2.34.2)
Requirement already satisfied: rpds-py==2026.9.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 42)) (2026.9.1)
Requirement already satisfied: six==1.17.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 43)) (1.17.0)
Requirement already satisfied: sniffio==1.3.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 44)) (1.3.1)
Requirement already satisfied: starlette==1.9.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 45)) (1.9.0)
Requirement already satisfied: tqdm==4.70.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 46)) (4.70.1)
Requirement already satisfied: typing-inspection==0.4.4 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 47)) (0.4.4)
Requirement already satisfied: typing_extensions==4.16.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 48)) (4.16.0)
Requirement already satisfied: urllib3==2.8.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 49)) (2.8.0)
Requirement already satisfied: uvicorn==0.54.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 50)) (0.54.0)
Requirement already satisfied: wcwidth==0.9.3 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 51)) (0.9.3)
Requirement already satisfied: websocket-client==1.9.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 52)) (1.9.0)
Requirement already satisfied: websockets==17.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 53)) (17.2)

[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: /private/tmp/gst-fresh-clone.ENfI58/.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m unittest discover -s tests -v
test_active_cheats_break_a_stock_identity (test_engine.GeneratorTests.test_active_cheats_break_a_stock_identity) ... ok
test_detection_factory_input_has_no_labels (test_engine.GeneratorTests.test_detection_factory_input_has_no_labels) ... ok
test_generated_data_sql_compatibility_smoke (test_engine.GeneratorTests.test_generated_data_sql_compatibility_smoke)
Exercise generator -> tables -> reconciliation views without Exasol. ... ok
test_generated_document_statuses_separate_decoys_from_fake_explanations (test_engine.GeneratorTests.test_generated_document_statuses_separate_decoys_from_fake_explanations) ... ok
test_officer_api_and_evaluator_share_rank_order (test_engine.GeneratorTests.test_officer_api_and_evaluator_share_rank_order) ... ok
test_officer_api_does_not_read_evaluation_labels (test_engine.GeneratorTests.test_officer_api_does_not_read_evaluation_labels) ... ok
test_problem_statement_unchanged (test_engine.GeneratorTests.test_problem_statement_unchanged) ... ok
test_retired_frontend_tokens_are_confined (test_engine.GeneratorTests.test_retired_frontend_tokens_are_confined) ... ok
test_seed_determinism_and_months (test_engine.GeneratorTests.test_seed_determinism_and_months) ... ok
test_sql_does_not_use_truth (test_engine.GeneratorTests.test_sql_does_not_use_truth) ... ok
test_confusion_counts (test_engine.GuardAndMetricsTests.test_confusion_counts) ... ok
test_injection_rejected (test_engine.GuardAndMetricsTests.test_injection_rejected) ... ok
test_no_positive_labels (test_engine.GuardAndMetricsTests.test_no_positive_labels) ... ok
test_template_select (test_engine.GuardAndMetricsTests.test_template_select) ... ok
test_clear_disposition_requires_verified_document (test_engine.SQLTests.test_clear_disposition_requires_verified_document) ... ok
test_hand_computed_stock (test_engine.SQLTests.test_hand_computed_stock) ... ok
test_independent_movement_corroborates (test_engine.SQLTests.test_independent_movement_corroborates) ... ok
test_two_checks_same_source_not_two_signals (test_engine.SQLTests.test_two_checks_same_source_not_two_signals) ... ok
test_window_checks_stock_continuity (test_engine.SQLTests.test_window_checks_stock_continuity) ... ok
test_swapped_fields (test_notes.NotesTest.test_swapped_fields) ... ok
test_tampered_note (test_notes.NotesTest.test_tampered_note) ... ok
test_unsupported_percentage (test_notes.NotesTest.test_unsupported_percentage) ... ok
test_valid_note (test_notes.NotesTest.test_valid_note) ... ok
test_written_numbers (test_notes.NotesTest.test_written_numbers) ... ok
test_api_factory_ids_and_followup_remain_bounded (test_site_data.SiteDataTests.test_api_factory_ids_and_followup_remain_bounded) ... ok
test_api_uses_only_the_restricted_connection (test_site_data.SiteDataTests.test_api_uses_only_the_restricted_connection) ... ok
test_snapshot_export_has_audited_evaluation_sources (test_site_data.SiteDataTests.test_snapshot_export_has_audited_evaluation_sources) ... ok

----------------------------------------------------------------------
Ran 27 tests in 0.292s

OK
exit: 0

## make reproduce
sh scripts/bootstrap.sh
Requirement already satisfied: annotated-types==0.8.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 1)) (0.8.0)
Requirement already satisfied: anyio==4.15.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 2)) (4.15.1)
Requirement already satisfied: attrs==26.1.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 3)) (26.1.0)
Requirement already satisfied: certifi==2026.10.18 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 4)) (2026.10.18)
Requirement already satisfied: cffi==2.1.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 5)) (2.1.1)
Requirement already satisfied: charset-normalizer==3.5.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 6)) (3.5.2)
Requirement already satisfied: click==8.5.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 7)) (8.5.0)
Requirement already satisfied: contourpy==1.4.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 8)) (1.4.0)
Requirement already satisfied: cryptography==50.0.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 9)) (50.0.2)
Requirement already satisfied: cycler==0.12.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 10)) (0.12.1)
Requirement already satisfied: distro==1.9.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 11)) (1.9.0)
Requirement already satisfied: fonttools==4.67.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 12)) (4.67.0)
Requirement already satisfied: h11==0.16.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 13)) (0.16.0)
Requirement already satisfied: httpcore==1.0.9 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 14)) (1.0.9)
Requirement already satisfied: httpx==0.28.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 15)) (0.28.1)
Requirement already satisfied: idna==3.20 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 16)) (3.20)
Requirement already satisfied: itsdangerous==2.2.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 17)) (2.2.0)
Requirement already satisfied: Jinja2==3.1.6 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 18)) (3.1.6)
Requirement already satisfied: jiter==0.17.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 19)) (0.17.0)
Requirement already satisfied: jsonschema==4.26.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 20)) (4.26.0)
Requirement already satisfied: jsonschema-specifications==2025.9.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 21)) (2025.9.1)
Requirement already satisfied: kiwisolver==1.5.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 22)) (1.5.1)
Requirement already satisfied: MarkupSafe==3.0.4 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 23)) (3.0.4)
Requirement already satisfied: matplotlib==3.10.8 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 24)) (3.10.8)
Requirement already satisfied: numpy==2.5.4 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 25)) (2.5.4)
Requirement already satisfied: openai==2.54.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 26)) (2.54.0)
Requirement already satisfied: packaging==26.3 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 27)) (26.3)
Requirement already satisfied: pandas==3.0.6 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 28)) (3.0.6)
Requirement already satisfied: pillow==12.3.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 29)) (12.3.0)
Requirement already satisfied: pip-licenses==5.5.5 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 30)) (5.5.5)
Requirement already satisfied: prettytable==3.18.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 31)) (3.18.0)
Requirement already satisfied: protobuf==7.36.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 32)) (7.36.2)
Requirement already satisfied: pycparser==3.11 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 33)) (3.11)
Requirement already satisfied: pydantic==2.14.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 34)) (2.14.1)
Requirement already satisfied: pydantic_core==2.50.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 35)) (2.50.1)
Requirement already satisfied: pyexasol==2.4.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 36)) (2.4.1)
Requirement already satisfied: pyparsing==3.3.3 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 37)) (3.3.3)
Requirement already satisfied: python-dateutil==2.9.0.post0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 38)) (2.9.0.post0)
Requirement already satisfied: python-multipart==0.0.32 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 39)) (0.0.32)
Requirement already satisfied: referencing==0.37.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 40)) (0.37.0)
Requirement already satisfied: requests==2.34.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 41)) (2.34.2)
Requirement already satisfied: rpds-py==2026.9.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 42)) (2026.9.1)
Requirement already satisfied: six==1.17.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 43)) (1.17.0)
Requirement already satisfied: sniffio==1.3.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 44)) (1.3.1)
Requirement already satisfied: starlette==1.9.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 45)) (1.9.0)
Requirement already satisfied: tqdm==4.70.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 46)) (4.70.1)
Requirement already satisfied: typing-inspection==0.4.4 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 47)) (0.4.4)
Requirement already satisfied: typing_extensions==4.16.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 48)) (4.16.0)
Requirement already satisfied: urllib3==2.8.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 49)) (2.8.0)
Requirement already satisfied: uvicorn==0.54.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 50)) (0.54.0)
Requirement already satisfied: wcwidth==0.9.3 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 51)) (0.9.3)
Requirement already satisfied: websocket-client==1.9.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 52)) (1.9.0)
Requirement already satisfied: websockets==17.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 53)) (17.2)

[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: /private/tmp/gst-fresh-clone.ENfI58/.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m src.provision_dashboard_reader
DASHBOARD_READER configured; label-free view grants are applied after reconciliation views exist. Secret was not printed.
.venv/bin/python -c "from src.db import connect; c=connect(); c.execute('DROP SCHEMA IF EXISTS GST_EVIDENCE CASCADE'); c.close()"
.venv/bin/python -m src.generate --scale medium --seed 51003 --out data/v3_c --fake-explanations
{"seed": 51003, "factories": 2400, "months": 12, "rows": {"factories": 2400, "suppliers": 2400, "factory_month": 28800, "invoices": 28695, "purchase_invoices": 28800, "eway_bills": 57600, "supplier_returns": 27360, "bank_entries": 57600, "machines": 2560, "supporting_documents": 12590, "truth": 28800}, "raw_evidence_rows": 241445, "noise_multiplier": 1.0, "missing_documents_rate": 0.0, "fake_explanations": true}
.venv/bin/python -m src.load_and_score --data data/v3_c --features data/v3_c/features.csv --report reports/reproduction_v3_c_load.json
Loaded factories: 0.100s
Loaded suppliers: 0.076s
Loaded factory_month: 0.179s
Loaded invoices: 0.247s
Loaded purchase_invoices: 0.181s
Loaded eway_bills: 0.203s
Loaded supplier_returns: 0.073s
Loaded bank_entries: 0.182s
Loaded machines: 0.089s
Loaded supporting_documents: 0.079s
{
  "manifest": {
    "seed": 51003,
    "factories": 2400,
    "months": 12,
    "rows": {
      "factories": 2400,
      "suppliers": 2400,
      "factory_month": 28800,
      "invoices": 28695,
      "purchase_invoices": 28800,
      "eway_bills": 57600,
      "supplier_returns": 27360,
      "bank_entries": 57600,
      "machines": 2560,
      "supporting_documents": 12590,
      "truth": 28800
    },
    "raw_evidence_rows": 241445,
    "noise_multiplier": 1.0,
    "missing_documents_rate": 0.0,
    "fake_explanations": true
  },
  "load_seconds": {
    "factories": 0.09991095900113578,
    "suppliers": 0.07620704100190778,
    "factory_month": 0.17882879200260504,
    "invoices": 0.24730420800187858,
    "purchase_invoices": 0.18079104100252152,
    "eway_bills": 0.2032957500014163,
    "supplier_returns": 0.07329633299741545,
    "bank_entries": 0.18178954199902364,
    "machines": 0.0885361250002461,
    "supporting_documents": 0.07929337500172551
  },
  "views": {
    "V_MATERIAL_OUTPUT": {
      "seconds": 0.21682379200137802,
      "rows": 7136,
      "checksum": 1465270.23074
    },
    "V_DISPATCH_INVOICE": {
      "seconds": 0.17061583399845404,
      "rows": 1940,
      "checksum": 411743.5058
    },
    "V_STOCK_ROLLFORWARD": {
      "seconds": 0.16938933300116332,
      "rows": 2731,
      "checksum": 758950.5458
    },
    "V_SUPPLIER_LOOP": {
      "seconds": 0.1799865419998241,
      "rows": 2646,
      "checksum": 2599106.8744
    },
    "V_RANKED_CASES": {
      "seconds": 0.19170775000020512,
      "rows": 28800,
      "checksum": 5877.435898482039
    },
    "V_SINGLE_SIGNAL_DISPOSITIONS": {
      "seconds": 0.31311291699967114,
      "rows": 28800,
      "checksum": 17523.0
    }
  },
  "actual_rows": {
    "factories": 2400,
    "suppliers": 2400,
    "factory_month": 28800,
    "invoices": 28695,
    "purchase_invoices": 28800,
    "eway_bills": 57600,
    "supplier_returns": 27360,
    "bank_entries": 57600,
    "machines": 2560,
    "supporting_documents": 12590
  },
  "join_sanity": {
    "duplicate_months": 0,
    "orphan_months": 0
  }
}
.venv/bin/python -c "from src.db import connect; c=connect(readonly=True); assert c.execute('SELECT COUNT(*) FROM GST_EVIDENCE.V_RANKED_CASES').fetchval()==28800; c.close()"
exit: 0

## make site (documented server)
exit: 0

## make live-smoke
sh scripts/bootstrap.sh
Requirement already satisfied: annotated-types==0.8.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 1)) (0.8.0)
Requirement already satisfied: anyio==4.15.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 2)) (4.15.1)
Requirement already satisfied: attrs==26.1.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 3)) (26.1.0)
Requirement already satisfied: certifi==2026.10.18 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 4)) (2026.10.18)
Requirement already satisfied: cffi==2.1.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 5)) (2.1.1)
Requirement already satisfied: charset-normalizer==3.5.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 6)) (3.5.2)
Requirement already satisfied: click==8.5.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 7)) (8.5.0)
Requirement already satisfied: contourpy==1.4.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 8)) (1.4.0)
Requirement already satisfied: cryptography==50.0.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 9)) (50.0.2)
Requirement already satisfied: cycler==0.12.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 10)) (0.12.1)
Requirement already satisfied: distro==1.9.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 11)) (1.9.0)
Requirement already satisfied: fonttools==4.67.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 12)) (4.67.0)
Requirement already satisfied: h11==0.16.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 13)) (0.16.0)
Requirement already satisfied: httpcore==1.0.9 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 14)) (1.0.9)
Requirement already satisfied: httpx==0.28.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 15)) (0.28.1)
Requirement already satisfied: idna==3.20 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 16)) (3.20)
Requirement already satisfied: itsdangerous==2.2.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 17)) (2.2.0)
Requirement already satisfied: Jinja2==3.1.6 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 18)) (3.1.6)
Requirement already satisfied: jiter==0.17.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 19)) (0.17.0)
Requirement already satisfied: jsonschema==4.26.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 20)) (4.26.0)
Requirement already satisfied: jsonschema-specifications==2025.9.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 21)) (2025.9.1)
Requirement already satisfied: kiwisolver==1.5.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 22)) (1.5.1)
Requirement already satisfied: MarkupSafe==3.0.4 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 23)) (3.0.4)
Requirement already satisfied: matplotlib==3.10.8 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 24)) (3.10.8)
Requirement already satisfied: numpy==2.5.4 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 25)) (2.5.4)
Requirement already satisfied: openai==2.54.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 26)) (2.54.0)
Requirement already satisfied: packaging==26.3 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 27)) (26.3)
Requirement already satisfied: pandas==3.0.6 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 28)) (3.0.6)
Requirement already satisfied: pillow==12.3.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 29)) (12.3.0)
Requirement already satisfied: pip-licenses==5.5.5 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 30)) (5.5.5)
Requirement already satisfied: prettytable==3.18.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 31)) (3.18.0)
Requirement already satisfied: protobuf==7.36.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 32)) (7.36.2)
Requirement already satisfied: pycparser==3.11 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 33)) (3.11)
Requirement already satisfied: pydantic==2.14.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 34)) (2.14.1)
Requirement already satisfied: pydantic_core==2.50.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 35)) (2.50.1)
Requirement already satisfied: pyexasol==2.4.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 36)) (2.4.1)
Requirement already satisfied: pyparsing==3.3.3 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 37)) (3.3.3)
Requirement already satisfied: python-dateutil==2.9.0.post0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 38)) (2.9.0.post0)
Requirement already satisfied: python-multipart==0.0.32 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 39)) (0.0.32)
Requirement already satisfied: referencing==0.37.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 40)) (0.37.0)
Requirement already satisfied: requests==2.34.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 41)) (2.34.2)
Requirement already satisfied: rpds-py==2026.9.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 42)) (2026.9.1)
Requirement already satisfied: six==1.17.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 43)) (1.17.0)
Requirement already satisfied: sniffio==1.3.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 44)) (1.3.1)
Requirement already satisfied: starlette==1.9.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 45)) (1.9.0)
Requirement already satisfied: tqdm==4.70.1 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 46)) (4.70.1)
Requirement already satisfied: typing-inspection==0.4.4 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 47)) (0.4.4)
Requirement already satisfied: typing_extensions==4.16.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 48)) (4.16.0)
Requirement already satisfied: urllib3==2.8.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 49)) (2.8.0)
Requirement already satisfied: uvicorn==0.54.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 50)) (0.54.0)
Requirement already satisfied: wcwidth==0.9.3 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 51)) (0.9.3)
Requirement already satisfied: websocket-client==1.9.0 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 52)) (1.9.0)
Requirement already satisfied: websockets==17.2 in ./.venv/lib/python3.14/site-packages (from -r requirements-lock.txt (line 53)) (17.2)

[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: /private/tmp/gst-fresh-clone.ENfI58/.venv/bin/python -m pip install --upgrade pip
.venv/bin/python scripts/live_smoke.py
{
  "time_utc": "2026-10-26T04:36:15Z",
  "base_url": "http://127.0.0.1:8876",
  "status": "passed",
  "health": {
    "mode": "Live",
    "time_utc": "2026-10-26T04:36:16Z",
    "git_sha": "f76345bc4f1670a2e6c68db6418f9a9b800f02d6",
    "query_timeout_seconds": 30,
    "row_limit": 200
  },
  "factory_id": "F000902",
  "outcomes": {
    "/case/F000902": {
      "status": 200,
      "evidence_rows": 22
    },
    "/note/F000902": {
      "status": 200,
      "validated": true,
      "evidence_rows": 22
    },
    "ask_dispatch": {
      "status": 200,
      "rows": 12,
      "sql": "SELECT PERIOD_MONTH,EXPECTED,OBSERVED,GAP,SEVERITY FROM GST_EVIDENCE.V_FEATURES WHERE FACTORY_ID='F000902' AND CHECK_FAMILY='dispatch_invoice' ORDER BY PERIOD_MONTH LIMIT 200"
    },
    "ask_timeline": {
      "status": 200,
      "rows": 12,
      "sql": "SELECT PERIOD_MONTH,SIGNAL_COUNT,TOTAL_SEVERITY,WEAKEST_LINK_NORMALISED_GAP,ESTIMATED_TAX_EXPOSURE_INR,STATUS FROM GST_EVIDENCE.V_RANKED_CASES WHERE FACTORY_ID='F000902' ORDER BY PERIOD_MONTH LIMIT 200"
    },
    "ask_evidence": {
      "status": 200,
      "rows": 22,
      "sql": "SELECT PERIOD_MONTH,CHECK_FAMILY,SOURCE_FAMILY,EXPECTED,OBSERVED,GAP,SEVERITY,DISCREPANCY_CLASS FROM GST_EVIDENCE.V_ALL_EVIDENCE WHERE FACTORY_ID='F000902' ORDER BY PERIOD_MONTH,CHECK_FAMILY LIMIT 200"
    },
    "injection": {
      "status": 400,
      "error": "SQL is not accepted. Ask for dispatch, timeline, or evidence in plain language."
    },
    "unknown_intent": {
      "status": 400,
      "error": "Fallback supports dispatch gap, timeline, or evidence questions. Try: show the dispatch gap by month."
    }
  },
  "parallel_ask": {
    "queries": 8,
    "latencies_seconds": [
      0.9071223749997444,
      1.0767017079997458,
      1.6725223749999714,
      1.7998020830018504,
      1.8306115410014172,
      1.8456816660000186,
      1.8999234160000924,
      1.9373153339984128
    ],
    "p50_seconds": 1.8152068120016338,
    "p95_seconds": 1.9242281626990008,
    "rows_each": [
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12
    ]
  },
  "activity_rows": 15
}
exit: 0


## Final result

Passed from a new local clone and virtual environment at source `f76345bc4f1670a2e6c68db6418f9a9b800f02d6`: network reachability, locked dependency installation, restricted-account provisioning, all tests, schema recreation and V3-C load, `make site`, and `make live-smoke`. The test used the author’s existing local Exasol Personal installation; a second machine has not yet been tested. Tag `submit-candidate-1` points to the tested source commit.
