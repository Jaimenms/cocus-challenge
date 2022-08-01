# Farming Simulator
Executes the farming simulator

This project corresponds to the second coding exercise of Cocus Challenge.

In this exercise we will be testing your multithreading skills.

Suppose that you want to simulate a fruit farm:
* Three farmers are collecting fruits from a single tree to a single dirty fruit basket.
* In parallel, three other farmers are getting the fruits from the dirty fruit basket, cleaning them, and pushing them into the single cleaned fruit basket.
* All the farmers are managing the fruit individually
* The tree has 50 fruits (and only one farmer at one time can pick fruit from the tree)
* Time to collect fruits from the trees into the basket: random(3,6) seconds
* Time to clean the fruits into the cleaned fruit basket: random(2,4) seconds
* The simulation ends when all the fruits from the tree are collected and cleaned.
* The number of fruits in the tree and in the baskets must be logged every second.

![Farming Diagram](./docs/images/farming_diagram.png)

# Quick Start

## Install

Clone this respository and run the following command:

```bash
pip install -r requirements.txt
```

## Use

Example 1: List all paths and file names inside _/var/tmp_ that have the suffix _.log_.

```bash
./farming_simulator.py
```

For more details about the syntax, please run:

```bash
farming_simulator.py --help
```

## Test

To run all unit tests, please run the following command:

```bash
python -m unittest
```