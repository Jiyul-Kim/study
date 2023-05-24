import React, {useState} from "react"
import './ExpenseForm.css'



const ExpenseForm = (props) => {
    const [enterdTitle, setEnterdTitle] = useState('')
    const [enterdAmount, SetenterdAmount] = useState('')
    const [enterdDate, setEnterdDate] = useState('')
    // const [userInput, setUserInput] = useState({
    //     enteredTitle: '',
    //     enteredAmount: '',
    //     enteredDate: ''
    // })

    const titleChangeHandler = (event) => {
        setEnterdTitle(event.target.value);
        // setUserInput({
        //     ...userInput,
        //     enteredTitle: event.target.value,    
        // })
    }
    const amountChangeHandler = (event) => {
        SetenterdAmount(event.target.value);
        // setUserInput({
        //     ...userInput,
        //     enteredAmount: event.target.value,    
        // })
    }
    const dateChangeHandler = (event) => {
        setEnterdDate(event.target.value);
        // setUserInput({
        //     ...userInput,
        //     enteredDate: event.target.value,    
        // })
    }

    const submitHandler= (event) => {
        event.preventDefault();

        const expenseData = {
            title: enterdTitle,
            amount : enterdAmount,
            date: new Date(enterdDate)
        };

        props.onSaveExpenseData(expenseData);
        setEnterdTitle('');
        SetenterdAmount('');
        setEnterdDate('');
    };  

    return <form onSubmit={submitHandler}>
        <div className="new-expense__controls">
            <div className="new-expense__control">
                <label>Title</label>
                <input type="text" value={enterdTitle} onChange={titleChangeHandler}/>
            </div>
            <div className="new-expense__control">
                <label>Amount</label>
                <input type="number" min="0.01" step="0.01" value={enterdAmount} onChange={amountChangeHandler}/>
            </div>
            <div className="new-expense__control">
                <label>Date</label>
                <input type="date" min="2019-01-01" max="2022-12-31" value={enterdDate} onChange={dateChangeHandler}/>
            </div>
        </div>
        <div className="new-expense__actions">
            <button type="submit">Add Expense</button>
        </div>
    </form>
}

export default ExpenseForm