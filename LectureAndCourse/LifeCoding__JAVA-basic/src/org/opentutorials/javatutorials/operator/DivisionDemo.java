package org.opentutorials.javatutorials.operator;

public class DivisionDemo {

	public static void main(String[] args) {
		int a = 10;
		int b = 3;
		
		float c = 10.0F;
		float d = 3.0F;
		
		// 정수 / 정수 라서 3
		System.out.println(a / b);
		// 실수 / 실수는 말 안해도 알겄지? 3.3333 이거 출력됨.
		System.out.println (c / d);
		/* 정수 / 실수에선 자바가 형변형을 해줌. 더 조밀하고 더 넓은 수를 표현할 수 있는
		그걸로 형변형이 됨.
		따라서 정수가 실수로 자동 형변형이 되는 거임.
		결과는 3.3333이 출력됨.
		*/
		System.out.println (a / d);
	}

}
