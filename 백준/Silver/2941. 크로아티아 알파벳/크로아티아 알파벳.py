# 1. Input data
target = input()

# 2. Output result
count = target.count("c=")          \
      + target.count("c-")          \
      + target.count("z=")          \
      + target.count("d-")          \
      + target.count("lj")          \
      + target.count("nj")          \
      + target.count("s=")

length = (len(target) -
       (target.count("c=") * 2
       + target.count("c-") * 2
       + target.count("z=") * 2
       + target.count("dz=") * 1
       + target.count("d-") * 2
       + target.count("lj") * 2
       + target.count("nj") * 2
       + target.count("s=") * 2))

print(count + length)
