# cli-toolkit
This is a command-line interface (CLI) application created using the click library in Python. It contains two entry points for a simple calculator and unit conversion tool. 

#### Calculator
Contains the 3 subcommands: sum for adding/subtracting a list of values provided, mult for multiplying 2 integers provided, div for dividing 2 integers entered

#### ConversionTool
It provides two subcommands: inches for converting inches to the desired metric unit

## Calculator:Usage
1. #### Sum:
  To sum a list of provided numbers 
```
CALC sum --ints 12,34,23
```
2. #### mult
   Multiplication of integers provided. 
```
CALC mult -n 2 -n 4
```
3. #### div
   Division of two integeres provided. 
```
CALC div -n1 3 -n2 9
```
## ConversionTool:Usage
1. #### inches
   To convert a length from inches to the desired metric unit. The subcommands `--inches` option followed by the length in inches. The `--type` option followed by the desired metric unit--options include ['m', 'dm', 'cm', 'mm', 'μm', 'nm']
```
CNVRS inches --inches 3 --type mm
```
# Requirements
* Python (3.10 or higher)
* `click` library(`pip install click`)

# How to Run 
1. Install the `click` library if you haven't already:
2. In the `cli-toolkit` directory and in a virtualenv install the toolkit:
```
python setup.py develop
```
3. Run the script with the desired subcommand and options
```
python your_script_name.py subcommand --option value
```

# Example
To sum a few ints provided in the cli
```
CALC sum --ints 12,34,23
```
console returns: 69

To convert 10 inches to centimeters:
```
CNVRS inches --inches 10 --type cm
```
console returns: `10in to 25.4cm`


