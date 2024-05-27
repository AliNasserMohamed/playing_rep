"""
This script reads a text file containing gift costs, calculates the total price of gifts
costing less than $25 after tax using both a for loop and NumPy, and compares their performance.

Usage:
- Ensure the file 'gift_costs.txt' exists in the same directory as this script.
- Run the script to compare the total prices calculated using a for loop and NumPy.

Output:
- The script prints the total price calculated using a for loop and NumPy, as well as the duration
  of each calculation."""
import time
import numpy as np


def read_txt_file(file_path):
    """
    Read a text file containing gift costs and convert the costs to integers.

    Args:
    - file_path (str): The path to the text file.

    Returns:
    - numpy.ndarray: An array containing the gift costs as integers.
    """
    with open(file_path,encoding="utf-8") as f:
        gift_costs = f.read().split('\n')
    gift_costs = np.array(gift_costs).astype(int)  # convert string to int
    return gift_costs

def sum_gift_costs_with_for(gift_costs):
    """
    Calculate the total price of gifts costing less than $25 after tax using a for loop.

    Args:
    - gift_costs (numpy.ndarray): An array containing the gift costs as integers.

    Returns:
    - float: The total price of gifts costing less than $25 after tax.
    """
    start = time.time()
    total_price = 0
    for cost in gift_costs:
        if cost < 25:
            total_price += cost * 1.08  # add cost after tax
    print('Duration for sum with for : {} seconds'.format(time.time() - start))
    return total_price

def sum_gift_costs_with_numpy(gift_costs):
    """
    Calculate the total price of gifts costing less than $25 after tax using NumPy.

    Args:
    - gift_costs (numpy.ndarray): An array containing the gift costs as integers.

    Returns:
    - float: The total price of gifts costing less than $25 after tax.
    """
    start = time.time()
    total_price = (gift_costs[gift_costs < 25]).sum() * 1.08
    print('Duration for sum with numpy: {} seconds'.format(time.time() - start))
    return total_price

def compare_for_vs_numpy(file_path):
    """
    Compare the performance of summing gift costs using a for loop vs. NumPy.

    Args:
    - file_path (str): The path to the text file containing gift costs.

    Returns:
    - None
    """
    gift_costs = read_txt_file(file_path)
    total_price_for = sum_gift_costs_with_for(gift_costs)
    total_price_numpy = sum_gift_costs_with_numpy(gift_costs)
    print(total_price_for)
    print(total_price_numpy)

if __name__ == "__main__":
    compare_for_vs_numpy('gift_costs.txt')
