Steps to create horobot

Prereqs: [prereqs](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli?pivots=programming-language-python&tabs=macos%2Cbash%2Cazure-cli#prerequisites)

```
python3.11 -m venv .venv
```


```
source .venv/bin/activate
```

```
func init --worker-runtime python
```

```
func new --name HttpTrigger --template "HTTP trigger" --authlevel "function"
```

