import argparse
import pkg_resources


def get_dependencies(package_name):
  dependencies = set()
  try:
    # Получаем список зависимостей
    dist = pkg_resources.get_distribution(package_name)
    for req in dist.requires():
      dependencies.add(req.project_name)
      dependencies.update(get_dependencies(req.project_name))
  except pkg_resources.DistributionNotFound:
    print(f"Package '{package_name}' not found.")
  return dependencies


def generate_plantuml(package_name, dependencies):
  plantuml_code = f'@startuml\n'
  plantuml_code += f'package "{package_name}" {{\n'
  for dep in dependencies:
    plantuml_code += f'  [ {dep} ]\n'
    plantuml_code += f'  [ {package_name} ] --> [ {dep} ]\n'
  plantuml_code += '}\n'
  plantuml_code += '@enduml'
  return plantuml_code


def main():
  parser = argparse.ArgumentParser(description='Visualize package dependencies as a PlantUML graph.')
  parser.add_argument('output_path', type=str, help='Path to the output file for the PlantUML code.')
  parser.add_argument('package_name', type=str, help='Name of the package to analyze.')

  args = parser.parse_args()

  dependencies = get_dependencies(args.package_name)
  plantuml_code = generate_plantuml(args.package_name, dependencies)

  # print(plantuml_code)

  with open(args.output_path, 'w') as f:
    f.write(plantuml_code)


if __name__ == '__main__':
  main()