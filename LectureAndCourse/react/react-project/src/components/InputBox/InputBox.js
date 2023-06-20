import styles from "./InputBox.module.css"

const InputBox = () => {
  return (
    <div className={styles.input_boxes}>
      <div className={styles.input_box}>
        <div className={styles.input_box_name}>이름</div>
        <input
          type="text"
          name="name"
          placeholder="이름"
          className={styles.input_box_input}
        />
      </div>
      <div className={styles.input_box}>
        <div className={styles.input_box_name}>전화번호</div>
        <input
          type="text"
          name="phone"
          placeholder="전화번호"
          className={styles.input_box_input}
        />
      </div>
      <div>
        <button className="input_box_button">저장</button>
      </div>
    </div>
  );
};

export default InputBox;