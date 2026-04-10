L = {"192.168.1.1", "192.168.1.2", "10.0.0.5"}
F = {"192.168.1.1", "192.168.1.5", "172.16.0.1"}
B = {"172.16.0.1", "8.8.8.8"}

both_but_not_blacklisted = (L & F) - B

attempted_but_never_succeeded = F - L

only_blacklisted = B - (L | F)

print(f"Both Successful & Failed (not blacklisted): {both_but_not_blacklisted}")
print(f"Attempted but never succeeded: {attempted_but_never_succeeded}")
print(f"Blacklisted only (no login attempts): {only_blacklisted}")