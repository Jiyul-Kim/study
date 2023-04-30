package org.opentutorials.javatutorials.operator;

public class ArithmeticDemo {

	public static void main(String[] args) {
		// result 는 3
		int result = 1 + 2;
		
		// result는 2
		result = result - 1;
		System.out.println(result);
		
		// result는 3
		result = result + 1;
		System.out.println(result);
		
		// result의 나머지는 1임
		result = result % 2;
		System.out.println(result);
	}

}
