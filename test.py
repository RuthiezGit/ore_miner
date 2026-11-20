import sys
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions & settings
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors (R, G, B)
BG_COLOR = (18, 18, 28)
PADDLE_COLOR = (70, 170, 255)
BALL_COLOR = (255, 255, 255)
TEXT_COLOR = (240, 240, 245)
BRICK_COLORS = [
    (235, 64, 52),   # Red
    (245, 130, 32),  # Orange
    (245, 200, 32),  # Yellow
    (60, 200, 110),  # Green
    (52, 152, 219),  # Blue
]

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 110, 14
PADDLE_SPEED = 8

# Ball settings
BALL_RADIUS = 8
BALL_SPEED = 5.5

# Brick grid settings
BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_PADDING = 6
BRICK_TOP_OFFSET = 60
BRICK_WIDTH = (WIDTH - BRICK_PADDING * (BRICK_COLS + 1)) // BRICK_COLS
BRICK_HEIGHT = 22

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 22, bold=True)
big_font = pygame.font.SysFont("arial", 44, bold=True)


def create_bricks():
    bricks = []
    for row in range(BRICK_ROWS):
        color = BRICK_COLORS[row % len(BRICK_COLORS)]
        for col in range(BRICK_COLS):
            x = BRICK_PADDING + col * (BRICK_WIDTH + BRICK_PADDING)
            y = BRICK_TOP_OFFSET + row * (BRICK_HEIGHT + BRICK_PADDING)
            bricks.append({"rect": pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT), "color": color})
    return bricks


def reset_game():
    paddle = pygame.Rect(
        (WIDTH - PADDLE_WIDTH) // 2,
        HEIGHT - 40,
        PADDLE_WIDTH,
        PADDLE_HEIGHT,
    )
    ball_pos = [WIDTH / 2, HEIGHT - 70]
    ball_vel = [BALL_SPEED * 0.7, -BALL_SPEED]
    bricks = create_bricks()
    score = 0
    lives = 3
    state = "PLAYING"  # PLAYING, GAME_OVER, WIN
    return paddle, ball_pos, ball_vel, bricks, score, lives, state


def draw_centered_text(text, font_obj, y_offset=0):
    surf = font_obj.render(text, True, TEXT_COLOR)
    rect = surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(surf, rect)


def main():
    paddle, ball_pos, ball_vel, bricks, score, lives, state = reset_game()

    while True:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r and state != "PLAYING":
                paddle, ball_pos, ball_vel, bricks, score, lives, state = reset_game()

        keys = pygame.key.get_pressed()

        if state == "PLAYING":
            # Move paddle
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                paddle.x -= PADDLE_SPEED
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                paddle.x += PADDLE_SPEED

            # Keep paddle inside screen
            paddle.x = max(0, min(WIDTH - PADDLE_WIDTH, paddle.x))

            # Move ball
            ball_pos[0] += ball_vel[0]
            ball_pos[1] += ball_vel[1]
            ball_rect = pygame.Rect(
                int(ball_pos[0] - BALL_RADIUS),
                int(ball_pos[1] - BALL_RADIUS),
                BALL_RADIUS * 2,
                BALL_RADIUS * 2,
            )

            # Wall collisions (left, right, top)
            if ball_pos[0] - BALL_RADIUS <= 0:
                ball_pos[0] = BALL_RADIUS
                ball_vel[0] *= -1
            elif ball_pos[0] + BALL_RADIUS >= WIDTH:
                ball_pos[0] = WIDTH - BALL_RADIUS
                ball_vel[0] *= -1

            if ball_pos[1] - BALL_RADIUS <= 0:
                ball_pos[1] = BALL_RADIUS
                ball_vel[1] *= -1

            # Bottom boundary (lose life)
            if ball_pos[1] - BALL_RADIUS > HEIGHT:
                lives -= 1
                if lives <= 0:
                    state = "GAME_OVER"
                else:
                    ball_pos = [paddle.centerx, paddle.top - BALL_RADIUS - 4]
                    ball_vel = [BALL_SPEED * 0.7, -BALL_SPEED]

            # Paddle collision with angle control based on hit position
            if ball_rect.colliderect(paddle) and ball_vel[1] > 0:
                hit_offset = (ball_pos[0] - paddle.centerx) / (PADDLE_WIDTH / 2)
                hit_offset = max(-1.0, min(1.0, hit_offset))
                ball_vel[0] = hit_offset * BALL_SPEED
                ball_vel[1] = -abs(ball_vel[1])
                ball_pos[1] = paddle.top - BALL_RADIUS

            # Brick collisions
            for brick in bricks[:]:
                if ball_rect.colliderect(brick["rect"]):
                    bricks.remove(brick)
                    score += 10
                    ball_vel[1] *= -1
                    break

            if not bricks:
                state = "WIN"

        # Drawing
        screen.fill(BG_COLOR)

        for brick in bricks:
            pygame.draw.rect(screen, brick["color"], brick["rect"], border_radius=4)

        pygame.draw.rect(screen, PADDLE_COLOR, paddle, border_radius=6)
        pygame.draw.circle(screen, BALL_COLOR, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

        # HUD
        hud_text = font.render(f"Score: {score}    Lives: {lives}", True, TEXT_COLOR)
        screen.blit(hud_text, (16, 16))

        if state == "GAME_OVER":
            draw_centered_text("GAME OVER", big_font, -30)
            draw_centered_text(f"Final Score: {score} — Press R to Restart", font, 25)
        elif state == "WIN":
            draw_centered_text("YOU WIN!", big_font, -30)
            draw_centered_text(f"Final Score: {score} — Press R to Play Again", font, 25)

        pygame.display.flip()


if __name__ == "__main__":
    main()