import click

from modules import coco2page_cli


@click.group()
@click.help_option("--help", "-h")
@click.version_option(
    "2.0",
    "-v", "--version",
    prog_name="HTRtools",
    message="%(prog)s v%(version)s - Developed at Centre for Philology and Digitality (ZPD), University of Würzburg"
)
def cli(**kwargs):
    """
    HTRtools main entry point.

    Developed at Centre for Philology and Digitality (ZPD), University of Würzburg.
    """

# analyse module
#cli.add_command(pagestats_cli)
#cli.add_command(pagesearch_cli)

# manipulation module
#cli.add_command(imgresize_cli)
#cli.add_command(pagefix_cli)

# parser module
cli.add_command(coco2page_cli)
#cli.add_command(csv2txt_cli)
#cli.add_command(img2png_cli)
#cli.add_command(ods2json_cli)
#cli.add_command(pdf2png_cli)

if __name__ == '__main__':
    cli()
