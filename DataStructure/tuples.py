# Values in Tuples are immutable, but we can reassign another values to the same tuple
dimensions :tuple[int,int] = (200,50)
dimensions[0]

dimensions = (100,100) #possible
#dimensions[1] = 10 #impossible
