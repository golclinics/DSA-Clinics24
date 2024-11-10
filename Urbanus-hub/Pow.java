import   java.util.Scanner;

public class Pow {
	public static boolean checkPow(int num) {
		int i;
		int flag = 0;
		double remainder=num;
		for (i = 0; i >= 0; i++) {
			remainder = remainder / 2;
			if (remainder == 1.0) {

				flag = 1;
				break;

			} else {
				if (remainder <1) {
					break;
				}
				flag = 0;
			}
		}
		if(flag == 1) {

			return true;
		} else {
			return false;
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
        System.out.println("Enter a number:");
		int num = input.nextInt();
		boolean bool = checkPow(num);
		System.out.println(bool);
		input.close();
	}

}