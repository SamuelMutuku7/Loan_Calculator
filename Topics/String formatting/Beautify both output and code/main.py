nickname = input()
profession = input()

stripped_nickname = nickname.strip()
stripped_profession = profession.strip()

print(f"http://example.com/{stripped_nickname}/desirable/{stripped_profession}/profile")