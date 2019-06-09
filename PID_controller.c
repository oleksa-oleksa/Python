#include <stdio.h>

/* 
By joining the P, I and D controller, we can take the advantages of the combined benefits from each controller. 

We have the P controller for fast system response, 
I controller to correct the steady state error and 
D controller to dampen the system and reduce overshoot.
*/

int main()
{
	while (1) {
		//Get the current position
		current_position = read_current_position();

		//Calculate the error
		error = target_position - current_position;

		// Error accumulation
		integral = integral + error;

		// Calculation error change
		derivative = error - last_error;

		//Calculate the control variable
		control_variable = kp * error + ki * integral + kd * derivative;

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

		// last error state for next loop iteration
		last_error = error;
	}
}