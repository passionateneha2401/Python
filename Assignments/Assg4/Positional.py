def Area(radius, PI):
    ans = PI * radius * radius
    return ans

def main():
    ret = Area(10.5,3.14)
    print("area of circle is: ",ret)

    ret = Area(13.6,7.12)
    print("area of circle is: ",ret)
    
if __name__ == "__main__":
    main()