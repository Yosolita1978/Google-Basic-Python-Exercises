import re

names = []

def open_file(filename):
  with open(filename, "rU") as my_file:
    text = my_file.read()
    return text

def extract_year(text):
  year_match = re.search(r"Popularity\sin\s(\d\d\d\d)", text)
  if not year_match:
    print "Couldn't find the year"
  year = year_match.group(1)
  return year

def extract_names(text):
  global names
  name_babies = re.findall(r"<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>", text)
  names_inrank = {}

  for line in name_babies:
    (rank, boyname, girlname) = line
    if boyname not in names_inrank:
      names_inrank[boyname] = rank
  
    if girlname not in names_inrank:
      names_inrank[girlname] = rank
    

  sorted_babies = sorted(names_inrank.keys())
  for name in sorted_babies:
    names.append(name + " " + names_inrank[name])
  return names

def print_names(list):
  global names
  for name in names[:51]:
    print name 

def menu():
  option_years = """
  Hello. Those are the years that we have available.
  1. 1990
  2. 1992
  3. 1994
  4. 1996
  5. 1998
  6. 2000
  7. 2002
  8. 2004
  9. 2006
  10. 2008

  """
  user_choices = raw_input(option_years)
  return user_choices


def main():
   user_choices = menu()
   if user_choices == "1":
    filename = "/Users/cristina/source/google-python-exercises/babynames/baby1990.html"
    text = open_file(filename)
    year = extract_year(text)
    print year
    names = extract_names(text)[:21]
    print_names(names)


  

  
if __name__ == '__main__':
  main()
