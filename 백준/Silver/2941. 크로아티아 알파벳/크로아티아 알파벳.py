# 1. Input data
target = input()

# 2. Output result
print((len(target) -
       (target.count("c=")
       + target.count("c-")
       + target.count("z=")
       + target.count("dz=")
       + target.count("d-")
       + target.count("lj")
       + target.count("nj")
       + target.count("s="))))
