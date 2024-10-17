# hangman_stages.py

stages = [
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / \\
       |
       ==========
    """,  # Stage 6: Full figure hanged
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / 
       |
       ==========
    """,  # Stage 5: One leg
    """
       --------
       |      |
       |      O
       |     /|\\
       |      
       |
       ==========
    """,  # Stage 4: Both arms
    """
       --------
       |      |
       |      O
       |     /|
       |      
       |
       ==========
    """,  # Stage 3: One arm
    """
       --------
       |      |
       |      O
       |      |
       |      
       |
       ==========
    """,  # Stage 2: Body
    """
       --------
       |      |
       |      O
       |     
       |      
       |
       ==========
    """,  # Stage 1: Head
    """
       --------
       |      |
       |      
       |     
       |      
       |
       ==========
    """  # Stage 0: Initial empty scaffold
]
