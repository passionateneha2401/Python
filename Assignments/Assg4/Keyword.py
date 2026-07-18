def Area(radius, PI):
    ans = PI * radius * radius
    return ans

def main():
    ret = Area(PI=3.14, radius=10.5)
    print("area of circle is: ",ret)
    
if __name__ == "__main__":
    main()

# all parameters should be keyword or positional...cause python is interpreted it will not get which para 
