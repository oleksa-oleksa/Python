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
#include "BUTTON.h"
#include "BUTTON_Private.h"
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


void drawEssentialScreen( unsigned int color )
{
	  GUI_SetBkColor( color );
	  GUI_Clear();

	  GUI_SetFont(&GUI_Font8x16);
	  GUI_SetTextMode(GUI_TM_NORMAL);

	  GUI_DrawGradientH(0, 0, 480, 16, 0x000000, 0x000000);

	  GUI_SetBkColor(0x000000);
	  GUI_DispStringAt("Ver. 0.05 Alpha", 190, 1);
}

void printFirstScreen()
{
	//0x862d2d
	  drawEssentialScreen( 0x862d2d );

	  int x1Pos[4], x2Pos[4];
	  int y1Pos[3], y2Pos[3];
	  for( int i = 0; i < 4; i++)					// generate drawn buttons
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
}

void cbForegroundWin( WM_MESSAGE * pMsg)
{
	switch(pMsg->MsgId)
	{
	case WM_PAINT:
		GUI_SetBkColor(GUI_GREEN);
		GUI_Clear();
		GUI_DispString( "Foreground window");
		break;
	default:
		WM_DefaultProc(pMsg);
	}
}
void menu1()
{
	int pressed = 0;
	drawEssentialScreen( 0x402060 );
	BUTTON_Handle myFirstButton = BUTTON_CreateEx(100, 50, 100, 40, 0, WM_CF_SHOW, 0, 1);
	BUTTON_SetText( myFirstButton, "Back");

/*
 	GUI_HWIN window;
	window = WM_CreateWindow( 10, 10, 100, 100, WM_CF_SHOW, cbForegroundWin, 0);
*/
	BUTTON_SetReactOnTouch();
	GUI_Delay( 1000 );
	if(myFirstButton){
		BUTTON_SetBkColor( myFirstButton, BUTTON_CI_UNPRESSED, 0xff6666);
	}
	while( 1 )
	{
		pressed = BUTTON_IsPressed(myFirstButton);

		if( pressed )
		{
			BUTTON_SetPressed( myFirstButton, 0);
			return;
		}
		GUI_Delay( 1000 );
	}
}

/***************************************************************************************/
void MainTask(void) {

	printFirstScreen();
	GUI_Delay( 500 );

  int x1Pos[4], x2Pos[4];
  int y1Pos[3], y2Pos[3];
  for( int i = 0; i < 4; i++)					// generate drawn buttons
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
	  				  /* go to menu1 */
	  				  if( (thisX > x1Pos[0]) && (thisX < x2Pos[0])
	  					&& (thisY > y1Pos[0]) && (thisY < y2Pos[0]) )
	  				  {
	  					  GUI_Clear();
	  					  menu1();

	  					  printFirstScreen();
	  			  		  thisX = -1;
	  			  		  thisY = -1;
	  				  }

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
	  	  }
	  	  else
	  	  {
	  		  thisX = -1;
	  		  thisY = -1;
	  	  }
  }

}

/*************************** End of file ****************************/
