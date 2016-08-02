Title: Python projects
Date: 2016-07-31
Category: Python

This folder is for Python stuff.

Making a virtual environment work in Sublime text:

1. Save as a new Project
2. Edit the projectname.sublime-project json script to include the path to the new build envitonment as follows:

``` javascript
{
 "folders":
 [
  {
   "path": "."
  }
 ],
 "virtualenv": "/Users/Tina/.virtualenvs/strengths",
 "build_systems": [
  {
   "name": "strengths",
   "cmd": ["/Users/Tina/.virtualenvs/strengths/bin/python", "$file"]
  }
 ] 
}
```
3. Select SHIFT+COMMAND+P to select the build system using build with.....
