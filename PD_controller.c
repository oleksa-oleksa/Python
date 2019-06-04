#include <stdio.h>

/* 
The derivative of any variable describes how that variable changes over time. 
In a PID controller, the derivative is the rate of change of the error. In digital form, it can be described as:

Derivative = Error – Last Error

Negative values of derivative indicate an improvement (reduction) in the error signal. 
For example, if the last error was 20 and the current error is 10, the derivative will be -10. 
When these negative values are multiplied with a constant, Kd, and are added to the output of the loop, 
it can slow down the system when approaching the target.

The damping effect of the D controller allows the system to have a higher value of Kp and/or Ki without overshooting. 
In consequent, this will give the system a better response time to set point changes. 

However, too high the value of Kd will also have negative effect. 
The D controller tense to amplify the noise exists in the feedback loop. 
If the Kd is too high, the system will become jerky if the feedback loop is noisy.

*/

int main()
{
	while (1) {
		//Get the current position
		current_position = read_current_position();

		// last error state
		last_error = error;

		//Calculate the error
		error = target_position - current_position;

		// Calculation error change
		derivative = error - last_error;

		//Calculate the control variable
		control_variable = kp * error + kd * derivative;

		// if CV is positive, run the motor clockwise and run forward
		// else run countercockwise and run backward
		if (control_variable > 0) {
			motor_pwm(control_variable);
		}
		else if (control_variable < 0) {
			motor_pwm(-control_variable);
		}
		else {
			motor_stop();
		}
	}
}