/*********************************************************************
*                SEGGER MICROCONTROLLER SYSTEME GmbH                 *
*        Solutions for real time microcontroller applications        *
**********************************************************************
*                                                                    *
*        (c) 1996 - 2015  SEGGER Microcontroller Systeme GmbH        *
*                                                                    *
*        Internet: www.segger.com    Support:  support@segger.com    *
*                                                                    *
**********************************************************************

***** emWin - Graphical user interface for embedded applications *****
emWin is protected by international copyright laws.   Knowledge of the
source code may not be used to write a similar product.  This file may
only be used in accordance with a license and should not be re-
distributed in any way. We appreciate your understanding and fairness.
----------------------------------------------------------------------
File        : BASIC_HelloWorld.c
Purpose     : Simple demo drawing "Hello world"
----------------------------------------------------------------------
*/

#include "GUI.h"

/*********************************************************************
*
*       Public code
*
**********************************************************************
*/
/*********************************************************************
*
*       MainTask
*/
void MainTask(void) {

  //GUI_SetPenSize( 20 );
  //GUI_DrawLine(10, 10, 400, 200);
  //GUI_SetPenSize(40);
  //GUI_DrawLine(400, 10, 10, 200);

  GUI_SetBkColor(0x862d2d);
  GUI_Clear();

  GUI_SetFont(&GUI_Font8x16);
  GUI_SetTextMode(GUI_TM_NORMAL);
//  GUI_SetColor(GUI_RED);

  GUI_DrawGradientH(0, 0, 480, 16, 0x000000, 0x000000);

  GUI_SetBkColor(0x000000);
  GUI_DispStringAt("Ver. 0.03 Alpha", 190, 1);




//  GUI_DrawGradientRoundedV(20, 0, 80, 60, 19, 0x4284f4, 0xFF4567);
//  GUI_DrawGradientRoundedV(20, 65, 80, 125, 19, 0x0000FF, 0x00FFFF);
  int x1Pos[4], x2Pos[4];
  int y1Pos[3], y2Pos[3];
  for( int i = 0; i < 4; i++)
  {
	  for (int j = 0; j < 3; j++)
	  {
		  x1Pos[i] = 30+i*88;
		  y1Pos[j] = 26+j*85;
		  x2Pos[i] = 94+i*88;
		  y2Pos[j] = 90+j*85;
		  GUI_DrawGradientRoundedV(x1Pos[i], y1Pos[j], x2Pos[i], y2Pos[j], 15, 0x0000FF, 0x00FFFF);
	  }
  }

  // touch screen
  int thisX, thisY, _TouchIsPressed;
  int thisColor = 0x000000;

  while(1)
  {
	  	  GUI_PID_STATE _TouchState;
	  	  _TouchIsPressed = GUI_TOUCH_GetState( &_TouchState);
	  	  if (_TouchIsPressed)
	  	  {
	  		  thisX = _TouchState.x;
	  		  thisY = _TouchState.y;

	  		  GUI_SetBkColor(thisColor);
	  		  thisColor += 0x10;
	  		  if (thisColor >= 0xFFFFFF)
	  		  {
	  			  thisColor = 0x123456;
	  		  }
	  		  for(int i = 0; i < 4; i++ )
	  		  {
	  			  for(int j = 0; j < 3; j++)
	  			  {
	  				  if( (thisX > x1Pos[i]) && (thisX < x2Pos[i])
	  					&& (thisY > y1Pos[j]) && (thisY < y2Pos[j]) )
	  				  {

	  					  GUI_DispCharAt( '1' + j, thisX, thisY);
	  					  GUI_DispCharAt( ',', thisX+6, thisY);
	  					  GUI_DispCharAt( '1' + i, thisX+12, thisY);
	  					  //GUI_DispStringAt("1,1", thisX, thisY);
	  				  }
	  			  }
	  		  }
	  		  /*
	  		  if (thisX > 20 && thisX < 80 && thisY > 0 && thisY < 60)
	  		  {
	  			GUI_DispStringAt("1,1", thisX, thisY);
	  		  }
	  		  if (thisX > 20 && thisX < 80 && thisY > 65 && thisY < 125)
	  		  {
	  			  GUI_DispStringAt("2", thisX, thisY);
	  		  }
	  		  if (thisX > 20 && thisX < 80 && thisY > 130 && thisY < 190)
	  		  {
	  			  GUI_DispStringAt("3", thisX, thisY);
	  		  }
	  		  if (thisX > 20 && thisX < 80 && thisY > 195 && thisY < 250)
	  		  {
	  			  GUI_DispStringAt("4", thisX, thisY);
	  		  }
	  		  */
	  	  }
	  	  else
	  	  {
	  		  thisX = -1;
	  		  thisY = -1;
	  	  }
  }

}

/*************************** End of file ****************************/
