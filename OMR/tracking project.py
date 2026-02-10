from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///fintrack.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
db = Session()


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    expenses = relationship("Expense", back_populates="category")


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    amount = Column(Integer)
    date = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="expenses")


class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True)
    month = Column(String, unique=True)
    limit = Column(Integer)


Base.metadata.create_all(engine)


def add_category():
    name = input("Category: ").strip()
    if not name:
        print("Category name required")
        return

    db.add(Category(name=name))
    db.commit()
    print("Category saved")


def add_expense():
    title = input("Title: ").strip()
    amount = input("Amount: ").strip()
    date = input("Date (YYYY-MM-DD): ").strip()
    category_id = input("Category ID: ").strip()

    if not (title and amount and date and category_id):
        print("Incomplete input")
        return

    db.add(
        Expense(
            title=title,
            amount=int(amount),
            date=date,
            category_id=int(category_id)
        )
    )
    db.commit()
    print("Expense recorded")


def update_expense():
    eid = input("Expense ID: ").strip()
    expense = db.query(Expense).filter_by(id=eid).first()

    if not expense:
        print("Expense not found")
        return

    expense.title = input("New title: ").strip()
    expense.amount = int(input("New amount: "))
    expense.date = input("New date: ").strip()
    db.commit()
    print("Expense updated")


def delete_expense():
    eid = input("Expense ID: ").strip()
    expense = db.query(Expense).filter_by(id=eid).first()

    if not expense:
        print("Expense not found")
        return

    db.delete(expense)
    db.commit()
    print("Expense removed")


def search_by_date():
    date = input("Date (YYYY-MM-DD): ").strip()
    records = db.query(Expense).filter_by(date=date).all()

    if not records:
        print("No expenses found")
        return

    for e in records:
        print(f"{e.title} | {e.amount}")


def category_report():
    query = """
    SELECT c.name, SUM(e.amount)
    FROM categories c
    JOIN expenses e ON c.id = e.category_id
    GROUP BY c.name
    """

    rows = db.execute(text(query)).fetchall()
    if not rows:
        print("No data available")
        return

    for name, total in rows:
        print(f"{name}: {total}")


def set_limit():
    month = input("Month (YYYY-MM): ").strip()
    limit = input("Limit: ").strip()

    if not (month and limit):
        print("Invalid input")
        return

    db.add(Budget(month=month, limit=int(limit)))
    db.commit()
    print("Budget saved")


def limit_alert():
    month = input("Month (YYYY-MM): ").strip()

    spent = db.execute(
        text("SELECT COALESCE(SUM(amount),0) FROM expenses WHERE date LIKE :m"),
        {"m": f"{month}%"}
    ).scalar()

    budget = db.query(Budget).filter_by(month=month).first()

    if not budget:
        print("No budget set")
        return

    if spent > budget.limit:
        print(f"Limit exceeded: {spent}/{budget.limit}")
    else:
        print(f"Within limit: {spent}/{budget.limit}")


def menu():
    print("""
1. Add category
2. Add expense
3. Update expense
4. Delete expense
5. Search by date
6. Category report
7. Set monthly budget
8. Budget alert
9. Exit
""")


while True:
    menu()
    choice = input("Select: ").strip()

    if choice == "1":
        add_category()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        update_expense()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        search_by_date()
    elif choice == "6":
        category_report()
    elif choice == "7":
        set_limit()
    elif choice == "8":
        limit_alert()
    elif choice == "9":
        print("Goodbye")
        break
    else:
        print("Try again")
