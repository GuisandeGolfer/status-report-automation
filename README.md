# How-To (Development)

+ going into the virtual environment that is inside 'statusreport-automation'

```python
source activate  
```
+ getting out of virtualenv

```python
deactivate 
```

+ this is how you can take a 'snapshot' of the current packages that are installed in the virtualenv 

```python
   
pip3 freeze > requirements.txt

```

+ requirements.txt => this is how you can save the packages that are installed without actually
      activating the virtualenv

```python

pipenv run pip3 freeze

```
