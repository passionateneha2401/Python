def Area(PI=3.14, radius):     #Error--SyntaxError
    ans = PI * radius * radius
    return ans

def main():
    ret = Area(10.5)
    print("area of circle is: ",ret)

    ret = Area(10.5, 7.12)
    print("area of circle is: ",ret)
    
if __name__ == "__main__":
    main()

# all parameters should be keyword or positional...cause python is interpreted it will not get which para 
