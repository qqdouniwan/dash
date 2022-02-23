import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)

false = False
true = True

fig = {
    "data":[{
        "x": [0, 1],
        "y": [0, 1.414],
        "name": "$E^2=m^2c^4+p^2c^2$"
    }, {
        "x": [0, 1],
        "y": [1.4, 0.1],
        "type": "bar",
        "name": "$x=\\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}$"
    }, {
        "type": "pie",
        "values": [1, 9],
        "labels": ["$\\frac{1}{10}=10\\%$", "$\\frac{9}{10}=90\\%$"],
        "domain": {"x": [0.3, 0.75], "y": [0.55, 1]}
    }, {
        "type": "heatmap",
        "z": [[1,2],[3,4]],
        "xaxis": "x2",
        "yaxis": "y2",
        "colorbar": {"y": 0.225, "len": 0.45}
    }],
    "layout": {
        "yaxis":{"domain": [0, 0.45], "title": {"text": "$y=\\sin{2 \\theta}$"}},
        "xaxis":{
            "domain": [0, 0.45],
            "title": {"text": "$x=\\int_0^a a^2+1$"},
            "tickvals": [0, 1],
            "ticktext": ["$\\frac{0}{100}$", "$\\frac{100}{100}$"]
        },
        "xaxis2": {"domain": [0.85, 1], "anchor": "y2"},
        "yaxis2": {
            "domain": [0, 0.45],
            "anchor": "x2",
            "title": {"text": "$(||01\\rangle+|10\\rangle)/\\sqrt2$"}
        },
        "height":500,
        "width":800,
        "margin": {"r": 250},
        "title": {"text": "$i\\hbar\\frac{d\\Psi}{dt}=-[V-\\frac{-\\hbar^2}{2m}\\nabla^2]\\Psi$"},
        "annotations":[
            {
                "text":"$(top,left)$","showarrow":false,"xref":"paper","yref":"paper",
                "xanchor":"left","yanchor":"top","x":0,"y":1,"textangle":10,
                "bordercolor":"#0c0","borderpad":3,"bgcolor":"#dfd"
            },
            {
                "text":"$(right,bottom)$","xref":"paper","yref":"paper",
                "xanchor":"right","yanchor":"bottom","x":0.2,"y":0.7,"ax":-20,"ay":-20,
                "textangle":-30,"bordercolor":"#0c0","borderpad":3,"bgcolor":"#dfd",
                "opacity":0.5
            },
            {"text":"$not-visible$", "visible": false},
            {
                "text":"$^{29}Si$","x":0.7,"y":0.7,"showarrow":false,
                "xanchor":"right","yanchor":"top"
            },
            {
                "text":"$^{17}O$","x":0.7,"y":0.7,"ax":15,"ay":-15,
                "xanchor":"left","yanchor":"bottom"
            }
        ]
    }
}

app.layout = html.Div(children=[

    dcc.Markdown('# h1 tag with inline MathJax: $E=mc^2$', mathjax=True),

    dcc.Markdown('''
        ## h2 tag with MathJax block:
        $$
        \\frac{1}{(\\sqrt{\\phi \\sqrt{5}}-\\phi) e^{\\frac25 \\pi}} =
        1+\\frac{e^{-2\\pi}} {1+\\frac{e^{-4\\pi}} {1+\\frac{e^{-6\\pi}}
        {1+\\frac{e^{-8\\pi}} {1+\\ldots} } } }
        $$
        ## Next line.
    ''', mathjax=True),

    dcc.Graph(
        mathjax=True,
        id='graph-with-math',
        figure=fig
    ),

    dcc.Markdown('### No MathJax: Apple: $2, Orange: $3'),

    dcc.Graph(
        id='graph-without-math',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
