import click

@click.group()
def cli():
    pass


def parse_list(ctx, params, value):
    if value is None:
        return []
    return value.split(',')

@cli.command()
@click.option('-nlist', '--ints',callback=parse_list, help='Enter a list of ints you would like to sum')
def sum(ints):
    ans = 0 
    for args in ints:
        ans += int(args)
    return click.echo(ans)

@cli.command()
@click.option('-n', '--ints', type=int, multiple=True, help='Enter integers to be multiplied')
def mult(ints):
    ans = 1 
    for args in ints:
        ans *= args
    return click.echo(ans)

@cli.command()
@click.option('-n1', '--int1', 'int1_' ,type=int, help='Enter 2 numbers to be divided')
@click.option('-n2', '--int2', 'int2_', type=int, help='Enter a number to divide' )
def div(**kwargs):
    try:
        ans = float(kwargs['int1_'])/float(kwargs['int2_'])
        return click.echo(ans)
    except: 
        click.echo("Cant divide by Zero")