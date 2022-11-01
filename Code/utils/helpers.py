def collision_test(rect, collision_rects):
    hit_list = []
    for collision_rect in collision_rects:
        if rect.colliderect(collision_rect):
            hit_list.append(collision_rect)
    return hit_list
