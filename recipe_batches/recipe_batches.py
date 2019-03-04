#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  needed = list(recipe.values())
  available = list(ingredients.values())
  if len(needed) > len(available):
    return 0
  batches = []
  for i in range(len(needed)):
    batches.append(available[i]//needed[i])
  sortBatches = sorted(batches)
  return sortBatches[0] 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))