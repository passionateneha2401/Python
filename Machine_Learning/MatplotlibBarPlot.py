import matplotlib.pyplot as plt


def main():
    Language = ["c","c++","java","python"]
    students = [30,40,35,55]

    plt.bar(
        Language,    #width of bars
        students,    #border color of bars
        width = 0.6, # width of bar border
        edgecolor="black",    #transperance 0.0 to 1.0
        linewidht=1,  # legend text
        alpha=0.8,
        label = "Students"
    )

    plt.title("Marvellous bar plot")
    plt.xlabel("Languages")
    plt.ylabel("no of students")

    plt.legend()

    plt.show()
    

if __name__ == "__main__":
    main()