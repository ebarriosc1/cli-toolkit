import click 

@click.group()
def cli():
    pass

@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f"Hello {name}")

@cli.command()
@click.option('--inches','inches_', type=int, help='Conversion from inches to centimeteres')
@click.option('--type','typeConv_', type=str, help='Enter the conversion of type of unit meters')
def inches(**kwargs):
    dictMeter = {'m':0.0254, 'dm':0.254, 'cm':2.54, 'mm':25.4, 'um':25400, 'nm':25e7 }
    if kwargs['typeConv_'] in dictMeter.keys():
        conversion = kwargs['inches_'] * dictMeter[kwargs['typeConv_']]
        return click.echo(f"{kwargs['inches_']}in to {conversion}{kwargs['typeConv_']}")
    else:
        click.echo('Please enter one of the following keys', dictMeter.keys())
