#include<stdio.h>
int main() {
	int number, temp;
	int a1,a2,a3,a4,a5;
	printf("Enter number : ");
	scanf("%d",&number);
	// printf("%d",number);
	temp = number;
	if (temp != 0) {
		a1 = temp%10;
		temp = temp/10;

		if (temp != 0) {
			a2 = temp%10;
			temp = temp/10;

			if (temp != 0) {
				a3 = temp%10;
				temp = temp/10;

				if (temp != 0) {
					a4 = temp%10;
					temp = temp/10;

					if (temp != 0) {
						a5 = temp%10;

						if (a1==a5 && a2==a4) {
							printf("Palindrome");
						} else {
							printf("Not Palindrome");
						}
					} else {
						if (a1 == a4 && a2 == a3) {
							printf("Palindrome");
						} else {
							printf("Not Palindrome");
						}
					}
				} else {
					if (a1==a3) {
						printf("Palindrome");
					} else {
						printf("Not Palindrome" );
					}
				}
			} else {
				if(a1 == a2) {
					printf("Palindrome");
				} else {
					printf("Not Palindrome");
				}
			}
		} else {
			printf("Palindrome");
		}
	}
	return 0;
}