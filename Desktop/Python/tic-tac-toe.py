int board[3][3];  // the board
    
// Initializes the game / board 
void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      board[i][j] = 0;
    }
  }
}

// Checks if there is a win condition
int checkWin() {
  for (int i = 0; i < 3; i++) {
    if (board[i][0] == board[i][1] && board[i][0] == board[i][2] && board[i][0] != 0) {
      return board[i][0];
    }
    if (board[0][i] == board[1][i] && board[0][i] == board[2][i] && board[0][i] != 0) {
      return board[0][i];
    }
  }
  if (board[0][0] == board[1][1] && board[0][0] == board[2][2] && board[0][0] != 0) {
    return board[0][0];
  }
  if (board[2][0] == board[1][1] && board[2][0] == board[0][2] && board[2][0] != 0) {
    return board[2][0];
  }
  return 0;
}

void loop() {
  // This is where you would handle player input and update the board
  // Then you could check if there's a win condition
  int result = checkWin();
  if (result != 0) {
    Serial.print("Player ");
    Serial.print(result);
    Serial.println(" wins!");
    delay(3000);
    setup();  // reset the game
  }
}