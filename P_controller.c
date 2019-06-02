#include <stdio.h>

/* The value of Kp needs to be chosen carefully in order 
to get the optimum system response. 
Lower values for Kp will tend to give smoother but slower responses. 

Higher values of Kp will yield much quicker response but may cause overshoot, 
where the output oscillates before settling.

Excessively high values of Kp may even throw the loop into an unstable state 
where the output oscillates without ever settling at the set point.

As can be seen from the graph of P controller, the actual position 
of the motor shaft, when settles down will not reach the target position. 
This is because when the current position is near to the target position, 
the error becomes very small and the computed PWM duty cycle is too small 
for the motor to overcome the friction and gravity. 
The small error that exists when the system has settled down is called the steady state error.

*/

int main()
{
	while (1) {
		//Get the current position
		current_position = read_current_position();

		//Calculate the error
		error = target_position - current_position;

		//Calculate the control variable
		control_variable = kp * error;

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