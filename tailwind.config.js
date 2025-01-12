/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        'site/templates/**/*.html'
    ],
    theme: {
        extend: {
            typography: {
                DEFAULT: {
                    css: {
                        a: {
                            color: '#fff',
                            '&:hover': {
                                color: 'rgb(45 212 191)',
                            },
                        },
                        ".codehilite": {
                            "border-radius": "0.25rem",
                        },
                    },
                },
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
