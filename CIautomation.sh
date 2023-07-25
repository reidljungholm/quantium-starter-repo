Last login: Mon Jul 24 23:42:48 on ttys004
Reids-MacBook-Air:~ reidljungholm$ cd ~/quantium-starter-repo
Reids-MacBook-Air:quantium-starter-repo reidljungholm$ source venv/bin/activate
(venv) Reids-MacBook-Air:quantium-starter-repo reidljungholm$ python3 testapp.py
/Users/reidljungholm/quantium-starter-repo/radiobutton.py:2: UserWarning: 
The dash_core_components package is deprecated. Please replace
`import dash_core_components as dcc` with `from dash import dcc`
  import dash_core_components as dcc
/Users/reidljungholm/quantium-starter-repo/radiobutton.py:3: UserWarning: 
The dash_html_components package is deprecated. Please replace
`import dash_html_components as html` with `from dash import html`
  import dash_html_components as html
(venv) Reids-MacBook-Air:quantium-starter-repo reidljungholm$ 
(venv) Reids-MacBook-Air:quantium-starter-repo reidljungholm$ # Capture the exit code of the test suite execution
(venv) Reids-MacBook-Air:quantium-starter-repo reidljungholm$ exit_code=$?
(venv) Reids-MacBook-Air:quantium-starter-repo reidljungholm$ 
(venv) Reids-MacBook-Air:quantium-starter-repo reidljungholm$ # Deactivate the virtual environment
(venv) Reids-MacBook-Air:quantium-starter-repo reidljungholm$ deactivate
Reids-MacBook-Air:quantium-starter-repo reidljungholm$ 
Reids-MacBook-Air:quantium-starter-repo reidljungholm$ # Return the exit code
Reids-MacBook-Air:quantium-starter-repo reidljungholm$ exit $exit_code

