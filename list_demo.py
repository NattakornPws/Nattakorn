

def demo():
    flowers = ["calla", "lily", "jasmine", "forget me not", 'ivy', 'gypso']
    #slice
    print(flowers[1:4])
    print(flowers[-1]) #-1 is the last index
    print(flowers[-1:-4:-2]) # -1 is the step

demo()

def operation():
    # How to define list
    flowers  = ["calla", "lily", "jasmine"]
    print(flowers)

    #Add member
    flowers = flowers + ["forget me not"]
    flowers.append("carnation")
    print(flowers)

    #Delete
    del flowers[1] # delete by index
    print(flowers)
    flowers.remove("jasmine") # delete by value
    print(flowers)

    #sort list
    flowers.sort()
    sorted_flowers = sorted(flowers)
    print(flowers)