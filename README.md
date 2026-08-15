 
# 🧩 **OOP-WRAPPER**

## 🧑‍💼 **Employee Management System**
A command-line Employee Management System built in Python using core Object-Oriented Programming concepts — Inheritance, Constructors, and Method Overriding — to model real-world relationships between a Person, an Employee, and a Manager.


---


## 🚀 **Project Overview**
This project showcases an **OOP-based Employee Management System** built entirely in core Python. It helps manage important employee information such as:

- 🙍 Name
- 🎂 Age
- 🆔 Employee ID
- 💰 Salary
- 🏢 Department

The program converts manual record-keeping into a simple, interactive terminal tool — showing how inheritance lets each class build on top of the one before it.


---


## 🧭 **Project Structure**
Here's how the classes and menu flow are organized in this project:
<img width="1440" height="920" alt="image" src="https://github.com/user-attachments/assets/96036a3d-e3e2-43ea-abaf-988b6cb96638" />




---


## 🔗 **Class Hierarchy**
```
Person
  └── name, age
  └── display()

Employee (inherits Person)
  └── employee_id, salary
  └── display()

Manager (inherits Employee)
  └── department
  └── display()
```


---


## 🗂️ **Project Files**
| File | Description |
|---|---|
| 🐍 `employee_management.py` | Main Python application file |
| 📘 `README.md` | Project documentation |


---


## 📋 **Menu Preview**
```
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit
```


---


## 🛠️ **Built With**
🐍 Core Python — Classes, Multi-level Inheritance, Constructors, Method Overriding, Loops & Conditionals. No external libraries needed.


---


## 📌 **Key Highlights**
- ✔ **Multi-level inheritance** done right — `Person → Employee → Manager`
- ✔ **`display()` overridden** at every level, showing polymorphism in action
- ✔ **Clean, beginner-friendly**, menu-driven CLI
- ✔ **Zero dependencies** — pure Python


---


## 🧬 **Data Model**

**🙍 Person**
```
name, age
```

**👔 Employee** (extends Person)
```
employee_id, salary
```

**🧑‍💼 Manager** (extends Employee)
```
department
```


---


## 🎯 **Use Cases**
This project can be used for:

- 📋 **Learning OOP fundamentals** (classes, objects, inheritance)
- 🧪 **Practicing class design** and reusability
- 👨‍💻 **Beginner portfolio** / academic project
- 🏢 **Understanding real-world hierarchies** (Person → Employee → Manager) modeled in code
- 🧠 **Practicing constructor chaining** and method overriding
- 🧾 **Small-scale employee record handling** for practice/demo purposes
- 🔧 **Base template** to extend into a bigger HR/employee management app


---


## ✅ **Requirements**
- 🐍 **Python 3.x** installed on your system
- 📦 **No additional packages** or installations needed
- 💻 **Any terminal or code editor** (VS Code, PyCharm, etc.)
- 🧩 **Basic Python syntax** helpful but not required


---


## ▶️ **How to Use**
```
python employee_management.py
```
Pick an option (1–5) and follow the prompts. Option 5 exits anytime.


---


## 🧠 **Learning Outcomes**
- 📐 **Designing a class hierarchy** using inheritance
- 🔗 **Calling a parent class's constructor** and methods explicitly
- 🔁 **Overriding methods** to extend, not replace, parent behavior
- 🔄 **Writing a clean menu-driven loop** for continuous interaction
- 🏗️ **Structuring a small OOP application** from scratch
- 🐞 **Debugging logic errors** in inherited methods
- 🌍 **Applying OOP concepts** to model real-world entities and relationships


---


## 🌟 **Future Enhancements**
- 🔹 **Fix `display()`** to use `self.salary` / `self.department`
- 🔹 **Fix exit logic** so it only breaks on option 5
- 🔹 **Persist data** with JSON / CSV / SQLite
- 🔹 **Support multiple records** + input validation
- 🔹 **Tkinter GUI version**


---


## 💻 **Sample Output**
<img width="1246" height="1971" alt="image" src="https://github.com/user-attachments/assets/7b3f90a2-e62f-418b-b725-a6377ed1910a" />





---


## 🤝 **Contributing**
PRs and ideas are welcome — fork it, tweak it, make it yours!


---


## 💬 **Feedback**
Found a bug or have a suggestion? Open an issue — feedback is always welcome!

Your inputs help make this project better for everyone learning OOP in Python.


---


## ⭐ **If You Like This Project**
🧑‍💼 Turning Simple Python Classes into a Real Management Tool — if it helped you, drop a ⭐!


---


## 👩‍💻 **Author**
Kavita Khushalani 📍India


---


🐍 Made with Python, for learning and fun.
