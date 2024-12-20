# thoughtful-robotic-factory

This is Nick Caravias's submission to the thoughtful AI sorting question.  

I typed the parametes to be floats, based on the description this made the most sense because of the decimals that 
could exist in the height, weight, etc.

## How to use  
### Test the method independently
To test the method independetly, simply import the sort method from the sort.py file and pass in the parameters. 

```
from sort import sort
# params are width, height, weight, mass
sort(100, 100, 100, 10)
```

### Use my pyunittest  
I created unit tests for this method as well. It covers all the scenarios and some edge cases. To run it in this repo, 
open your terminal at the root level and run:   

```
$ python3 -m unittest tests/test_sort.py
```
