# FIFO Animal Shelter

Animal Shelter that takes only dogs or cats and can return the dog or cat that has been in the shelter longest, depending on the species requested.

# Challenge

Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
Implement the following methods:
enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.
