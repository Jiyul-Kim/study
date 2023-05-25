import React, {state, useState} from "react"
import './NewExpense.css'
import './ExpenseForm'
import ExpenseForm from "./ExpenseForm"

const NewExpense = (props) => {
    const [isEdting, setIsEdting] = useState(false);
    const saveExpenseDataHandler = (enteredExpenseData) => {
        const expenseData = {
            ...enteredExpenseData,
            id: Math.random().toString()
            
        }
        props.onAddExpense(expenseData)
        
      
    }
    const startEditingHandler = () => {
        setIsEdting(true)
    }       

    const stopEdtingHandler = () => {
        setIsEdting(false)
    }
    
    return <div className="new-expense">
        {!isEdting && <button onClick={startEditingHandler}>Add new Expense</button>}
       {isEdting && <ExpenseForm onSaveExpenseData={saveExpenseDataHandler} onCancel={stopEdtingHandler}/>}
    </div>
}
export default NewExpense