import React, {useState} from "react";

import ExpenseItem from "./ExpenseItem";
import Card from "../UI/Card";
import './Expense.css';
import './ExpensesFilter'
import ExpensesFilter from "./ExpensesFilter";

function Expense (props){

    const [filteredYear, setFilteredYear] = useState('2020')

    const filterChangeHandler = selecteYear => {
      setFilteredYear(selecteYear)
      
    }

   const filteredExpenses = props.item.filter(expense => {
    return expense.date.getFullYear().toString() === filteredYear
   })
    
    return (
        <Card className="expenses">
            <ExpensesFilter selected={filteredYear} onChangeFilter={filterChangeHandler}/>

            {filteredExpenses.map((expense) => (
              <ExpenseItem 
                key={expense.id}
                title={expense.title}
                amount={expense.amount}
                date={expense.date}
              />
              
            ))}
            
            
        </Card >
    )
}


export default Expense;