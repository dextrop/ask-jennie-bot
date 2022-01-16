import os

from jennie.responses import *
from jennie.helper import check_if_angular_project

navbar_light = '''<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>'''

navbar_dark = navbar_light.replace("navbar-light bg-light", "navbar-dark bg-dark")
navbar_primary = navbar_light.replace("navbar-light bg-light", "navbar-dark bg-primary")


BASE_DIRECTORY = "src/app/uigallery/"

HTML_NAVBAR_LIGHT = "navbarlight/navbarlight.component.html"
HTML_NAVBAR_DARK = "navbardark/navbardark.component.html"
HTML_NAVBAR_PRIMARY = "navbarprimary/navbarprimary.component.html"
HTML_NAVBAR_CUSTOM = "navbarcustom/navbarcustom.component.html"

class Navbar():
    def __init__(self, type):
        self.type = type

    def add_bootstrap_navbar(self):
        self.current_dir = os.getcwd()
        if check_if_angular_project(self.current_dir):
            if self.type == "navbar-light":
                os.system("ng g c uigallery/navbarlight --skip-tests=true")
                open(BASE_DIRECTORY + HTML_NAVBAR_LIGHT, "w").write(navbar_light)

            elif self.type == "navbar-dark":
                os.system("ng g c uigallery/navbardark --skip-tests=true")
                open(BASE_DIRECTORY + HTML_NAVBAR_DARK, "w").write(navbar_dark)

            elif self.type == "navbar-primary":
                os.system("ng g c uigallery/navbarprimary --skip-tests=true")
                open(BASE_DIRECTORY + HTML_NAVBAR_PRIMARY, "w").write(navbar_primary)

            elif self.type[0] == "#" and len(self.type) == 7:
                os.system("ng g c uigallery/navbarcustom --skip-tests=true")
                replace = '''bg-light">'''
                replace_with = '''navbar-light" style="background-color: #e3f2fd;>'''
                navbar_custom = navbar_light.replace(replace, replace_with)
            else:
                print ("Unknown Navbar Type")
        else:
            print (UNKNOWN_PROJECT_TYPE)


