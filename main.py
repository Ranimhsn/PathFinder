import pygame
from algorithms import bfs, dijkstra, a_star
def create_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]
def draw_grid(screen, grid, cell_size, start, end, explored, path):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            x = col * cell_size
            y = row * cell_size
            cell = (row, col)
            if grid[row][col] == 1:
                color = (45, 45, 55)
            elif cell in path:
                color = (255, 205, 60)
            elif cell in explored:
                color = (130, 190, 245)
            else:
                color = (248, 249, 252)
            pygame.draw.rect(
                screen,
                color,
                (x, y, cell_size, cell_size)
            )
            pygame.draw.rect(
                screen,
                (215, 218, 225),
                (x, y, cell_size, cell_size),
                1
            )
            if start == cell:
                pygame.draw.rect(
                    screen,
                    (50, 190, 100),
                    (x, y, cell_size, cell_size)
                )
            if end == cell:
                pygame.draw.rect(
                    screen,
                    (225, 75, 75),
                    (x, y, cell_size, cell_size)
                )
def handle_mouse_click(
    grid,
    cell_size,
    start,
    end,
    placing_end
):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    row = mouse_y // cell_size
    col = mouse_x // cell_size
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        if placing_end:
            if grid[row][col] == 0:
                end = (row, col)
            placing_end = False
        elif pygame.mouse.get_pressed()[0]:
            if (row, col) != start and (row, col) != end:
                grid[row][col] = 1
        elif pygame.mouse.get_pressed()[2]:
            if grid[row][col] == 0:
                start = (row, col)
    return start, end, placing_end
def run_algorithm(grid, start, end, algorithm):
    if start is None or end is None:
        return [], []
    if algorithm == "BFS":
        return bfs(grid, start, end)
    elif algorithm == "Dijkstra":
        return dijkstra(grid, start, end)
    elif algorithm == "A*":
        return a_star(grid, start, end)
    return [], []
def draw_panel(
    screen,
    font,
    small_font,
    algorithm,
    explored,
    path
):
    pygame.draw.rect(
        screen,
        (238, 240, 245),
        (600, 0, 400, 600)
    )
    pygame.draw.line(
        screen,
        (200, 203, 210),
        (600, 0),
        (600, 600),
        2
    )
    title = font.render(
        "PATHFINDER",
        True,
        (25, 30, 40)
    )
    screen.blit(title, (635, 28))
    subtitle = small_font.render(
        "Algorithm Visualizer",
        True,
        (100, 105, 115)
    )
    screen.blit(subtitle, (637, 62))
    pygame.draw.line(
        screen,
        (200, 203, 210),
        (635, 95),
        (965, 95),
        2
    )
    algorithm_label = small_font.render(
        "SELECTED ALGORITHM",
        True,
        (100, 105, 115)
    )
    screen.blit(
        algorithm_label,
        (635, 120)
    )
    algorithm_name = algorithm if algorithm else "None"
    algorithm_text = font.render(
        algorithm_name,
        True,
        (35, 85, 150)
    )
    screen.blit(
        algorithm_text,
        (635, 145)
    )
    controls_title = small_font.render(
        "CONTROLS",
        True,
        (100, 105, 115)
    )
    screen.blit(
        controls_title,
        (635, 205)
    )
    controls = [
        ("B", "BFS"),
        ("D", "Dijkstra"),
        ("A", "A*"),
        ("E", "Set arrival"),
        ("SPACE", "Run algorithm"),
    ]
    y = 235
    for key, description in controls:
        pygame.draw.rect(
            screen,
            (220, 224, 232),
            (635, y, 55, 27),
            border_radius=5
        )
        key_text = small_font.render(
            key,
            True,
            (35, 40, 50)
        )
        screen.blit(
            key_text,
            (645, y + 3)
        )
        description_text = small_font.render(
            description,
            True,
            (55, 60, 70)
        )
        screen.blit(
            description_text,
            (705, y + 3)
        )
        y += 34
    mouse_text = small_font.render(
        "Left click  →  Obstacle",
        True,
        (55, 60, 70)
    )
    screen.blit(
        mouse_text,
        (635, 410)
    )
    mouse_text = small_font.render(
        "Right click →  Start",
        True,
        (55, 60, 70)
    )
    screen.blit(
        mouse_text,
        (635, 438)
    )
    pygame.draw.line(
        screen,
        (200, 203, 210),
        (635, 475),
        (965, 475),
        2
    )
    results_title = small_font.render(
        "RESULTS",
        True,
        (100, 105, 115)
    )
    screen.blit(
        results_title,
        (635, 492)
    )
    explored_text = small_font.render(
        "Nodes explored : " + str(len(explored)),
        True,
        (40, 45, 55)
    )
    screen.blit(
        explored_text,
        (635, 520)
    )
    path_text = small_font.render(
        "Path length    : " + str(len(path)),
        True,
        (40, 45, 55)
    )
    screen.blit(
        path_text,
        (635, 548)
    )
    legend = [
        ((50, 190, 100), "Start"),
        ((225, 75, 75), "End"),
        ((45, 45, 55), "Obstacle"),
        ((130, 190, 245), "Explored"),
        ((255, 205, 60), "Path")
    ]
    x = 25
    y = 570
    for color, name in legend:
        pygame.draw.rect(
            screen,
            color,
            (x, y, 12, 12)
        )
        x += 16
        text = small_font.render(
            name,
            True,
            (30, 35, 45)
        )
        screen.blit(
            text,
            (x, y - 5)
        )
        x += 65
def reset_project():
    grid = create_grid(20, 20)
    start = None
    end = None
    algorithm = None
    path = []
    explored = []
    animation_running = False
    animation_index = 0
    placing_end = False
    return (
        grid,
        start,
        end,
        algorithm,
        path,
        explored,
        animation_running,
        animation_index,
        placing_end
    )
pygame.init()
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)
pygame.display.set_caption(
    "PathFinder - Algorithm Visualizer"
)
font = pygame.font.Font(
    None,
    36
)
small_font = pygame.font.Font(
    None,
    22
)
grid = create_grid(20, 20)
cell_size = 30
start = None
end = None
algorithm = None
path = []
explored = []
animation_running = False
animation_index = 0
placing_end = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not animation_running:
                start, end, placing_end = handle_mouse_click(
                    grid,
                    cell_size,
                    start,
                    end,
                    placing_end
                )
        if event.type == pygame.KEYDOWN:
            # BFS
            if event.key == pygame.K_b:

                algorithm = "BFS"

            # Dijkstra
            elif event.key == pygame.K_d:
                algorithm = "Dijkstra"

            # A*
            elif event.key == pygame.K_a:
                algorithm = "A*"

            # Set arrival
            elif event.key == pygame.K_e:

                placing_end = True
            elif event.key == pygame.K_SPACE:

                if not animation_running:
                    path, explored = run_algorithm(
                        grid,
                        start,
                        end,
                        algorithm
                    )
                    animation_index = 0
                    animation_running = True

            # Reset
            elif event.key == pygame.K_r:

                grid = create_grid(20, 20)
                start = None
                end = None
                algorithm = None
                path = []
                explored = []
                animation_running = False
                animation_index = 0
                placing_end = False
    if animation_running:
        if animation_index < len(explored):
            animation_index += 1
        else:
            animation_running = False
    visible_explored = explored[:animation_index]
    screen.fill(
        (215, 218, 225)
    )
    draw_grid(
        screen,
        grid,
        cell_size,
        start,
        end,
        visible_explored,
        path if not animation_running else []
    )
    draw_panel(
        screen,
        font,
        small_font,
        algorithm,
        visible_explored,
        path if not animation_running else []
    )
    pygame.display.flip()
    pygame.time.delay(30)
pygame.quit()




